import os
import qrcode
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
qr_data_url = os.getenv('QR_DATA_URL', 'https://github.com/Sathvik2199')
qr_code_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
qr_code_filename = os.getenv('QR_CODE_FILENAME', 'github_qr_code.png')
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')

# Ensure the directory for saving QR codes exists
qr_code_path = Path(qr_code_dir)
qr_code_path.mkdir(parents=True, exist_ok=True)

# Generate and save the QR code
def generate_qr_code(data_url, save_path, fill_color, back_color):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    img.save(save_path)
    logging.info(f"QR code saved at {save_path}")

if __name__ == "__main__":
    save_path = qr_code_path / qr_code_filename
    generate_qr_code(qr_data_url, save_path, fill_color, back_color)