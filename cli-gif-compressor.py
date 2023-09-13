# Notes in code courtesy of ChatGPT-4
# Trust me, you didn't want to see what it looked like before...

import argparse
import os
from PIL import Image, UnidentifiedImageError
import imageio

def compress_gif(input_path, output_path, shrinkage_modifier, frame_resize=0.8, skip_frames=1):
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: The specified input file '{input_path}' does not exist.")
        return

    # Check original file size
    try:
        original_size = os.path.getsize(input_path)
    except Exception as e:
        print(f"Error: Could not get the file size of '{input_path}'. {e}")
        return

    temp_webp_path = "temp.webp"
    temp_gif_path = "temp.gif"

    # Preprocess by resizing and reducing frame count
    try:
        with imageio.get_reader(input_path) as reader:
            frames = [Image.fromarray(frame) for i, frame in enumerate(reader) if i % skip_frames == 0]
            if frame_resize != 1.0:
                frames = [frame.resize([int(dim * frame_resize) for dim in frame.size]) for frame in frames]
            imageio.mimsave(temp_gif_path, [frame for frame in frames], format="gif")
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return

    input_path = temp_gif_path  # New input path is the resized/reduced GIF

    while True:
        try:
            # Convert GIF to WebP
            imageio.mimwrite(temp_webp_path, imageio.mimread(input_path, memtest=False), format="webp")

            # Convert WebP back to GIF
            imageio.mimwrite(temp_gif_path, imageio.mimread(temp_webp_path, memtest=False), format="gif")
        except Exception as e:
            print(f"Error during conversion: {e}")
            return

        compressed_size = os.path.getsize(temp_gif_path)

        # Check if desired shrinkage is reached
        if original_size / compressed_size >= shrinkage_modifier:
            os.rename(temp_gif_path, output_path)
            os.remove(temp_webp_path)
            print("Operation completed successfully.")
            return
        else:
            input_path = temp_gif_path  # Set input for next iteration to the compressed GIF

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Losslessly compress a GIF using WebP.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("input_path", type=str, help="Path to the input GIF file.")
    parser.add_argument("output_path", type=str, help="Path where the compressed GIF will be saved.")
    parser.add_argument("-m", "--shrinkage_modifier", type=float, default=1.2, 
                        help="Factor by which you want to shrink the file size. E.g., 1.2 means you want the output file to be at most 1/1.2 of the original.")
    parser.add_argument("-r", "--frame_resize", type=float, default=0.8, 
                        help="Factor to resize each frame. Values should be between 0 and 1.")
    parser.add_argument("-s", "--skip_frames", type=int, default=1, 
                        help="Skip frames during reading to reduce the frame count. Value should be greater than 0.")
    
    args = parser.parse_args()
    
    compress_gif(args.input_path, args.output_path, args.shrinkage_modifier, args.frame_resize, args.skip_frames)