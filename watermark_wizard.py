#!/usr/bin/env python3
"""
Watermark Wizard - Batch Image Watermarking Tool
Author: Anvith N (2025A7PS0916H)

This script applies a text or logo watermark to all images in a given folder.
Supports batch processing, position control, adjustable opacity, and offset in %.
"""

import os
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png")


def apply_text_watermark(image, text, position, opacity, size, offset):
    """Apply a text watermark to an image."""
    watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark_layer)

    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x, y = get_position(position, image.size, (text_width, text_height), offset)
    draw.text((x, y), text, font=font, fill=(255, 255, 255, opacity))

    return Image.alpha_composite(image.convert("RGBA"), watermark_layer)


def apply_logo_watermark(image, logo_path, position, opacity, size, offset):
    """Apply a logo watermark to an image."""
    logo = Image.open(logo_path).convert("RGBA")

    # Resize logo to given % of image dimensions
    a = int(image.width * (size / 100))
    b = int(image.height * (size / 100))
    scale = max(a, b)
    logo.thumbnail((scale, scale))

    # Adjust opacity
    if opacity < 255:
        alpha = logo.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity / 255)
        logo.putalpha(alpha)

    x, y = get_position(position, image.size, logo.size, offset)

    watermark_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    watermark_layer.paste(logo, (x, y), logo)

    return Image.alpha_composite(image.convert("RGBA"), watermark_layer)


def get_position(position, image_size, wm_size, offset):
    """Calculate (x, y) coordinates for watermark placement with offset."""
    img_w, img_h = image_size
    wm_w, wm_h = wm_size

    # Convert percentage offset to pixels
    off_x = int(img_w * (offset[0] / 100))
    off_y = int(img_h * (offset[1] / 100))

    if position == "top-left":
        return off_x, off_y
    elif position == "top-right":
        return img_w - wm_w - off_x, off_y
    elif position == "bottom-left":
        return off_x, img_h - wm_h - off_y
    elif position == "bottom-right":
        return img_w - wm_w - off_x, img_h - wm_h - off_y
    elif position == "center":
        return (img_w - wm_w) // 2 + off_x, (img_h - wm_h) // 2 + off_y
    else:
        raise ValueError(f"Unsupported position: {position}")


def process_images(input_folder, output_folder, text, logo, position, opacity, size, offset):
    """Process all images in the input folder and save watermarked versions."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(SUPPORTED_FORMATS):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                if logo:
                    watermarked = apply_logo_watermark(img, logo, position, opacity, size, offset)
                else:
                    watermarked = apply_text_watermark(img, text, position, opacity, size, offset)

                watermarked.convert("RGB").save(output_path)
                print(f"✅ Saved: {output_path}")


def parse_offset(value):
    """Parse offset argument (e.g., '5,3') into tuple (x%, y%)."""
    try:
        parts = [float(v.strip()) for v in value.split(",")]
        if len(parts) != 2:
            raise ValueError
        return tuple(parts)
    except ValueError:
        raise argparse.ArgumentTypeError("Offset must be in format 'x,y' (percentages).")


def main():
    parser = argparse.ArgumentParser(
        description="Watermark Wizard - Batch Image Watermarking Tool"
    )
    parser.add_argument("input_folder", help="Path to input folder containing images")
    parser.add_argument("output_folder", help="Path to save watermarked images")
    parser.add_argument("--text", default="Watermark", help="Watermark text")
    parser.add_argument("--position", default="bottom-right",
                        choices=["top-left", "top-right", "bottom-left", "bottom-right", "center"],
                        help="Position of watermark")
    parser.add_argument("--opacity", type=int, default=128, help="Opacity (0-255)")
    parser.add_argument("--logo", help="Path to logo image (overrides text watermark)")
    parser.add_argument("--size", type=float, default=20,
                        help="Size of logo as percentage of image width")
    parser.add_argument("--offset", type=parse_offset, default=(1, 1),
                        help="Offset from corner in percentages, e.g. '5,3'")

    args = parser.parse_args()

    process_images(
        args.input_folder,
        args.output_folder,
        args.text,
        args.logo,
        args.position,
        args.opacity,
        args.size,
        args.offset
    )


if __name__ == "__main__":
    main()
