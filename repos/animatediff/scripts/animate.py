import argparse
import datetime
import inspect
import os
from omegaconf import OmegaConf

import torch

import diffusers
from diffusers import AutoencoderKL, DDIMScheduler

from tqdm.auto import tqdm
from transformers import CLIPTextModel, CLIPTokenizer

from ..animatediff.models.unet import UNet3DConditionModel
from ..animatediff.pipelines.pipeline_animation import AnimationPipeline
from ..animatediff.utils.util import save_videos_grid
from ..animatediff.utils.convert_from_ckpt import convert_ldm_unet_checkpoint, convert_ldm_clip_checkpoint, convert_ldm_vae_checkpoint
from ..animatediff.utils.convert_lora_safetensor_to_diffusers import convert_lora
from diffusers.utils.import_utils import is_xformers_available

from einops import rearrange, repeat

import csv, pdb, glob
from safetensors import safe_open
import math
from pathlib import Path
import shutil
import gc
import cv2

def save_frames_from_video(video_path, output_dir):
    """
    This function saves frames from a video file to a given directory.

    Parameters:
    video_path (str): The path to the video file.
    output_dir (str): The directory to save the frames.
    """

    # Create the frames folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened correctly
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
    else:
        # Frame index
        i = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imwrite(f'{output_dir}/{str(i).zfill(4)}.png', frame)
            i += 1

    cap.release()
    cv2.destroyAllWindows()

def main(args,window):
    *_, func_args = inspect.getargvalues(inspect.currentframe())
    func_args = dict(func_args)

    # print("args", args)

    if args.context_length == 0:
        args.context_length = args.L
    if args.context_overlap == -1:
        args.context_overlap = args.context_length // 2


    time_str = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    savedir = f"outputs/{Path(args.config).stem}-{time_str}"
    os.makedirs(savedir)
    inference_config = OmegaConf.load(args.inference_config)

    config  = OmegaConf.load(args.config)
    samples = []
    
    sample_idx = 0

    for model_idx, (config_key, model_config) in enumerate(list(config.items())):
        
        motion_modules = model_config.motion_module
        motion_modules = [motion_modules] if isinstance(motion_modules, str) else list(motion_modules)
        for motion_module in motion_modules:
        
            ### >>> create validation pipeline >>> ###
            tokenizer    = CLIPTokenizer.from_pretrained(args.pretrained_model_path, subfolder="tokenizer")
            text_encoder = CLIPTextModel.from_pretrained(args.pretrained_model_path, subfolder="text_encoder")
            vae          = AutoencoderKL.from_pretrained(args.pretrained_model_path, subfolder="vae")            
            unet         = UNet3DConditionModel.from_pretrained_2d(args.pretrained_model_path, subfolder="unet", unet_additional_kwargs=OmegaConf.to_container(inference_config.unet_additional_kwargs))

            if is_xformers_available(): unet.enable_xformers_memory_efficient_attention()
            else: assert False

            pipeline = AnimationPipeline(
                window=window,
                vae=vae, text_encoder=text_encoder, tokenizer=tokenizer, unet=unet,
                scheduler=DDIMScheduler(**OmegaConf.to_container(inference_config.noise_scheduler_kwargs)),
                scan_inversions=not args.disable_inversions,
            ).to("cuda")

            # 1. unet ckpt
            # 1.1 motion module
            motion_module_state_dict = torch.load(motion_module, map_location="cpu")
            if "global_step" in motion_module_state_dict: func_args.update({"global_step": motion_module_state_dict["global_step"]})
            missing, unexpected = pipeline.unet.load_state_dict(motion_module_state_dict, strict=False)
            assert len(unexpected) == 0
            
            # 1.2 T2I
            if model_config.path != "":
                if model_config.path.endswith(".ckpt"):
                    state_dict = torch.load(model_config.path)
                    pipeline.unet.load_state_dict(state_dict)
                    
                elif model_config.path.endswith(".safetensors"):
                    state_dict = {}
                    with safe_open(model_config.path, framework="pt", device="cpu") as f:
                        for key in f.keys():
                            state_dict[key] = f.get_tensor(key)
                            
                    is_lora = all("lora" in k for k in state_dict.keys())
                    if not is_lora:
                        base_state_dict = state_dict
                    else:
                        base_state_dict = {}
                        with safe_open(model_config.base, framework="pt", device="cpu") as f:
                            for key in f.keys():
                                base_state_dict[key] = f.get_tensor(key)                
                    
                    # vae
                    converted_vae_checkpoint = convert_ldm_vae_checkpoint(base_state_dict, pipeline.vae.config)
                    pipeline.vae.load_state_dict(converted_vae_checkpoint)
                    # unet
                    converted_unet_checkpoint = convert_ldm_unet_checkpoint(base_state_dict, pipeline.unet.config)
                    pipeline.unet.load_state_dict(converted_unet_checkpoint, strict=False)
                    # text_model
                    pipeline.text_encoder = convert_ldm_clip_checkpoint(base_state_dict)
                    
                    # import pdb
                    # pdb.set_trace()
                    if is_lora:
                        pipeline = convert_lora(pipeline, state_dict, alpha=model_config.lora_alpha)

            pipeline.to("cuda")
            ### <<< create validation pipeline <<< ###

            prompts      = model_config.prompt
            n_prompts    = list(model_config.n_prompt) * len(prompts) if len(model_config.n_prompt) == 1 else model_config.n_prompt
            init_image   = model_config.init_image if hasattr(model_config, 'init_image') else None
            
            random_seeds = model_config.get("seed", [-1])
            random_seeds = [random_seeds] if isinstance(random_seeds, int) else list(random_seeds)
            random_seeds = random_seeds * len(prompts) if len(random_seeds) == 1 else random_seeds
            
            config[config_key].random_seed = []
            window.write_event_value('-total_samples_progress_bar-',len(prompts))

            for propt_idx, (prompt, n_prompt, random_seed) in enumerate(zip(prompts, n_prompts, random_seeds)):
                
                # manually set random seed for reproduction
                if random_seed != -1: torch.manual_seed(random_seed)
                else: torch.seed()
                config[config_key].random_seed.append(torch.initial_seed())
                
                print(f"current seed: {torch.initial_seed()}")
                print(f"sampling {prompt} ...")
                sample = pipeline(
                    window,
                    prompt,
                    init_image          = init_image,
                    negative_prompt     = n_prompt,
                    num_inference_steps = model_config.steps,
                    guidance_scale      = model_config.guidance_scale,
                    width               = args.W,
                    height              = args.H,
                    video_length        = args.L,
                    temporal_context    = args.context_length,
                    strides             = args.context_stride + 1,
                    overlap             = args.context_overlap,
                    fp16                = not args.fp32,
                ).videos
                samples.append(sample)
                outpout_dir_name = "sample"
                prompt = "-".join((prompt.replace("/", "").split(" ")[:10]))
                save_videos_grid(sample, f"{savedir}/results/mp4/{sample_idx}-{prompt}.mp4")
                print(f"save to {savedir}/results/{prompt}.mp4")

                if args.save_gif_format:
                    save_videos_grid(sample, f"{savedir}/results/gif/{sample_idx}-{prompt}.gif")
                    print(f"save to {savedir}/results/{prompt}.gif")

                if args.save_video_frames:
                    save_frames_from_video(f"{savedir}/results/mp4/{sample_idx}-{prompt}.mp4", f"{savedir}/results/frames/{sample_idx}-{prompt}")
                    print(f"save frames to {savedir}/results/frames/{sample_idx}-{prompt}")

                window.write_event_value('-single_video_generated-',f"{savedir}/results/mp4/{sample_idx}-{prompt}.mp4")
                window.write_event_value('-sample_progress_bar-',sample_idx)
                
                sample_idx += 1

    samples = torch.concat(samples)
    save_videos_grid(samples, f"{savedir}/results_grid.mp4", n_rows=4)
    
    del pipeline
    gc.collect()
    torch.cuda.empty_cache()
    OmegaConf.save(config, f"{savedir}/config.yaml")
    # window.write_event_value('-video_grid_generated-',f"{savedir}/results_grid.mp4")
    window.write_event_value('-video_grid_generated-',f"{savedir}/results/mp4")

