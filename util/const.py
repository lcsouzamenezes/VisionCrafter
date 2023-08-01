NAME = "VisionCrafter"
VER = '0.0.2'
GITHUB = "github.com/diStyApps/VisionCrafter"
MODEL = None
USE_FADE_IN = True
WIN_MARGIN = 60

# colors
WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS = 10000

# Base64 Images to use as icons in the window
img_error = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cbM9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAhyDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUCAJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkbmHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UWmq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
img_success = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaMZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZasJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQAAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAADnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNVgnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAqZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvlc4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='
patreon = b'iVBORw0KGgoAAAANSUhEUgAAAFwAAAAZCAYAAAC8ekmHAAAACXBIWXMAAC4jAAAuIwF4pT92AAAF8WlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDggNzkuMTY0MDM2LCAyMDE5LzA4LzEzLTAxOjA2OjU3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjEuMCAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIyLTExLTI4VDE3OjQ5OjEwKzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMi0xMS0yOFQxODowMjo1MCswMjowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMi0xMS0yOFQxODowMjo1MCswMjowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4NDM1ODVmZS1iOTMwLTcwNGItYmYwMy1mNTgzNDZiOTQ2ZjMiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDowYmMyNTI5Zi02YTg0LWM2NDMtOTI0Ny0yYmFiN2FlZTgzNzkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo0NWZlNjdhOC0yZGI5LTdlNDQtODM0ZS03YmY1MzA3MTk1NTkiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjQ1ZmU2N2E4LTJkYjktN2U0NC04MzRlLTdiZjUzMDcxOTU1OSIgc3RFdnQ6d2hlbj0iMjAyMi0xMS0yOFQxNzo0OToxMCswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIDIxLjAgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo4NDM1ODVmZS1iOTMwLTcwNGItYmYwMy1mNTgzNDZiOTQ2ZjMiIHN0RXZ0OndoZW49IjIwMjItMTEtMjhUMTg6MDI6NTArMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMS4wIChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4gLKG0AAALtElEQVRoge2ae5RV1X3HP/u87rn33MfM3BkYhmGY8JhBIMFRUWiBMWpkWWtDtIrRmj6URqJNzUqbtqxkta6ExD9c6rKUZag0sZrGphURbVBriVJQiOIMOqAgMDPMMMMwb+7r3PPa/eNyh8fM8MjCNNV+1zpr3bvPvvu392f/9m//zr5HrFy5Etu2FymK8hgwG5CAz0WSQGK6Gblt5m2ZAxUNlpUfEher7f8DUgEBYq8IlD93VXu75vv+tUKI16SUH5NNiSwodOL6mOz8JktejhJs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'
GRAY_9900 = '#0A0A0A'
COLOR_GREEN = '#43CD80'
COLOR_DARK_GREEN2 = '#78BA04'
COLOR_DARK_GREEN = '#74a549'
COLOR_BLUE = '#69b1ef'
COLOR_RED = '#E74555'
COLOR_RED_ORANGE = '#C13515'
COLOR_ORANGE ='#FE7639'
COLOR_PURPLE = '#a501e8'
COLOR_DARK_GRAY = '#1F1F1F'
COLOR_DARK_BLUE = '#4974a5'
# DARK_GREEN = '#78BA04'
LIGHT_GRAY = '#6d6d6d'
GRAY = "#2A2929"
GRAY2 = "#121212"

# GRAY_1111 = '#111111'
# LIGHT_BLUE = '#69b1ef'
# RED_ORANGE = '#C13515'
# PURPLE = '#583e82'
# GREEN = '#43CD80'
TERMINAL_BLUE = '#0099ff'
TERMINAL_GREEN = '#00ff00'
TERMINAL_GREEN2 = '#00cc00'
DIM_GREEN = '#69823c'
DIM_BLUE = '#4974a5'
image_file_ext = {
    ("IMAGE Files", "*.png"),
    ("IMAGE Files", "*.jpg"),
    ("IMAGE Files", "*.jpeg"),
}

video_file_ext = {
    ("Video Files", "*.mp4"),
    ("Video Files", "*.webm"),
    ("Video Files", "*.gif"),
}
extensions = [".safetensors"]


 