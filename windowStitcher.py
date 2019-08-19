#!/usr/bin/env python3

"""
    Anthony Nelzin-Santos
    anthony@nelzin.fr
    https://anthony.nelzin.fr

    European Union Public License 1.2
"""

import argparse
from PIL import Image

def paste_window(background, window, padding):
    background = Image.open(background)
    window = Image.open(window)
    window.thumbnail((1200, 1200))
    
    position = ((background.width - window.width) // 2, (background.height - window.height) // 2)
    background.paste(window, position, window)

    left = (background.width - window.width)/2-padding
    top = (background.height - window.height)/2-padding
    right = (background.width + window.width)/2+padding
    bottom = (background.height + window.height)/2+padding
    crop = (left,top,right,bottom)
    
    final_img = background.crop(crop)
    final_img.save("output.png")

def main():
    parser = argparse.ArgumentParser(description="Paste a capture of a window on top of the specified background.")
    parser.add_argument("background", help="Path to the background image.")
    parser.add_argument("window", help="Path to the window screen capture (PNG with transparency mask for best results).")
    parser.add_argument("-p", "--padding", help="Padding around the final crop.", type=int)
    
    args = parser.parse_args()
    if args.padding:
        padding = args.padding
    else:
        padding = 0

    paste_window(args.background, args.window, padding)
    
if __name__ == '__main__':
    main()