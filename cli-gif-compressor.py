import argparse
from PIL import Image, UnidentifiedImageError
import os

def reduce_frame_count(input_path, output_path, skip_frames=1):
    try:
        image = Image.open(input_path)
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return
    except UnidentifiedImageError:
        print(f"Error: '{input_path}' is not a valid image file.")
        return
    
    if not image.format == 'GIF':
        print(f"Error: '{input_path}' is not a GIF.")
        return

    if skip_frames < 1:
        print("Error: Number of frames to skip must be at least 1.")
        return

    frames = []
    frame_count = 0
    
    try:
        while True:
            if frame_count % skip_frames == 0:
                frames.append(image.copy())
            
            image.seek(image.tell() + 1)
            frame_count += 1
    except EOFError:
        pass

    try:
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)
    except Exception as e:
        print(f"Error: Could not save the output file. {e}")
    
    print("Operation completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress a GIF by reducing the frame count.")
    
    parser.add_argument("input_path", type=str, help="Path to the input GIF")
    parser.add_argument("output_path", type=str, help="Path to save the output GIF")
    parser.add_argument("-s", "--skip_frames", type=int, default=1, help="Number of frames to skip")
    
    args = parser.parse_args()
    
    reduce_frame_count(args.input_path, args.output_path, args.skip_frames)