import qrcode

url = input("Enter the URL: ")

qr = qrcode.make(url)

qr.save("qrcode.png")

print("QR code generated and saved as qrcode.png")