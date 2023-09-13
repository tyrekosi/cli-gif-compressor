# cli-gif-compressor
Simple Python CLI tool to compress gifs by converting them to WEBPs

Slightly improve version of one of these I made for a personal project.

# Usage
usage: `cli-gif-compressor.py [-h] [-m SHRINKAGE_MODIFIER] [-r FRAME_RESIZE] [-s SKIP_FRAMES] input_path output_path`

Losslessly compress a GIF using WebP.

```positional arguments:
  input_path            Path to the input GIF file.
  output_path           Path where the compressed GIF will be saved.

options:
  -h, --help            show this help message and exit
  -m SHRINKAGE_MODIFIER, --shrinkage_modifier SHRINKAGE_MODIFIER
                        Factor by which you want to shrink the file size. E.g., 1.2 means you want the output file to be at most 1/1.2 of the original. (default: 1.2)
  -r FRAME_RESIZE, --frame_resize FRAME_RESIZE
                        Factor to resize each frame. Values should be between 0 and 1. (default: 0.8)
  -s SKIP_FRAMES, --skip_frames SKIP_FRAMES
                        Skip frames during reading to reduce the frame count. Value should be greater than 0. (default: 1)
```