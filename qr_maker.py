import qrcode
from PIL import Image
import argparse
import os


def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)


def resize_image(input_image_path, output_image_path, output_width):
    with Image.open(input_image_path) as image:
        width_percent = (output_width / float(image.size[0]))
        output_height = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((output_width, output_height), Image.LANCZOS)
        image.save(output_image_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate and resize a QR code.")
    parser.add_argument("url", help="The URL to encode in the QR code.")
    parser.add_argument("--output", default="output/qr_code.png",
                        help="The output file for the QR code image.")
    parser.add_argument("--resized_output", default="output/resized_qr_code.png",
                        help="The output file for the resized QR code image.")
    parser.add_argument("--width", type=int, default=500,
                        help="The width for the resized QR code image.")

    args = parser.parse_args()

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Generate and save the QR code
    generate_qr_code(args.url, args.output)

    # Resize and save the QR code
    resize_image(args.output, args.resized_output, output_width=args.width)

    print(f"QR code generated and saved as '{args.output}'.")
    print(f"Resized QR code saved as '{args.resized_output}'.")
