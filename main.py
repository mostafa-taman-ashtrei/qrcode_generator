import qrcode
import os

if not os.path.exists('./qrcodes'): os.mkdir('./qrcodes')

qr_data = input('Enter the qr data: ')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


img.save('./qrcodes/code.png')