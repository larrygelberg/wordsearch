#!/usr/bin/env python3
from PIL import Image
import numpy as np
import sys
import os

def img_to_dotzero_threshold(path, out_width=120, threshold=250):
    # Load and convert to grayscale
    img = Image.open(path).convert('L')
    w, h = img.size
    aspect = 0.75  # adjust for character aspect ratio (monospaced font)
    out_height = int((h / w) * out_width * aspect)
    img = img.resize((out_width, max(1, out_height)), Image.LANCZOS)
    arr = np.array(img)
    chars = np.where(arr <= threshold, '0', '.')
    lines = [''.join(row) for row in chars]
    return '\n'.join(lines)

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {os.path.basename(sys.argv[0])} <image_file> <width>")
        sys.exit(1)

    image_path = sys.argv[1]
    try:
        out_width = int(sys.argv[2])
    except ValueError:
        print("Width must be an integer.")
        sys.exit(1)

    if not os.path.isfile(image_path):
        print(f"Error: file '{image_path}' not found.")
        sys.exit(1)

    output = img_to_dotzero_threshold(image_path, out_width)
    print(output)

if __name__ == '__main__':
    main()
