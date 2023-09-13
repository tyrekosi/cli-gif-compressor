# CLI-GIF-Compressor

A simple Python CLI tool for compressing GIFs by converting them to WebP format. This is an improved version of a tool originally created for a personal project. *Not* lossless.

## Installation

1. `git clone git@github.com:tyrekosi/cli-gif-compressor.git`
2. `pip install -r requirements.txt`

You should be good to go and to run the script. If you're going to use this more than once I recommend creating a more convenient setup though... 

## Usage

### _Linux/MacOS_

`python3 cli-gif-compressor.py [-h] [-m SHRINKAGE_MODIFIER] [-r FRAME_RESIZE] [-s SKIP_FRAMES] input_path output_path`

### _Windows_

`python cli-gif-compressor.py [-h] [-m SHRINKAGE_MODIFIER] [-r FRAME_RESIZE] [-s SKIP_FRAMES] input_path output_path`

### Args

| Argument                         | Description                                                        | Default Value  |
| ---------------------------------| ------------------------------------------------------------------ | -------------- |
| `input_path` (Positional)        | The path to the input GIF file.                                    |                |
| `output_path` (Positional)       | The path where the compressed GIF will be saved.                   |                |
| `-h`, `--help`                   | Display the help message and exit.                                 |                |
| `-m`, `--shrinkage_modifier`     | Factor by which you want to shrink the file size. E.g., setting this to 1.2 means you want the output file to be at most 1/1.2 of the original size. | 1.2            |
| `-r`, `--frame_resize`           | Factor to resize each frame. Value should be between 0 and 1.      | 0.8            |
| `-s`, `--skip_frames`            | Number of frames to skip during reading to reduce the frame count. Value should be greater than 0. | 1              |

## Example

_Linux/MacOS_

`python3 cli-gif-compressor.py -m 1.2 -r 0.8 -s 2 input.gif output.gif`

_Windows_

`python cli-gif-compressor.py -m 1.2 -r 0.8 -s 2 input.gif output.gif`

This command will compress `input.gif` to produce `output.gif`, aiming for a file size that's roughly 1/1.2 (.8333...) of the original, resizing each frame by a factor of 0.8, and skipping every 2nd frame.