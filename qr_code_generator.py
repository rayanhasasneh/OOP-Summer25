import qrcode

# URL you want to encode
url = "https://rayan-warsaw-webspace.lovable.app"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (in boxes)
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("rayan_webspace_qr.png")

print("QR code generated and saved as 'rayan_webspace_qr.png'")
