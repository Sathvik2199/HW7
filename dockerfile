# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container to /app/qrdocker
WORKDIR /app/qrdocker

# Copy the Python script into the /app/qrdocker directory
COPY main.py .

# Install necessary Python packages
RUN pip install qrcode[pil]

# Set environment variables with defaults
ENV QR_DATA_URL="https://github.com/Sathvik2199"
ENV QR_CODE_DIR="qr_codes"
ENV QR_CODE_FILENAME="github_qr_code.png"
ENV FILL_COLOR="blue"
ENV BACK_COLOR="white"

# Create directory for QR codes
RUN mkdir -p /app/qrdocker/${QR_CODE_DIR}

# Entrypoint to run the QR code generator script
ENTRYPOINT ["python", "main.py"]