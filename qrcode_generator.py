import qrcode

# ✅ Replace with your current Ngrok URL
url = " http://bit.ly/4kypKzW  "

# ✅ Create QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# ✅ Save the QR image
img.save("phishing_qr.png")

print("✅ QR code generated successfully!")
