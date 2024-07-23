import qrcode 
from PIL import Image


qr  = qrcode.QRCode(version=1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 10,border = 4, )

str = input("Give Input For QR :- ")
qr.add_data(str)
qr.make(fit=True)

image = qr.make_image(fill_color = "yellow", back_color= "black")
image.save("ProjectsPY/QRCODES/new.png")

# image.save("ProjectsPY/QRCODES/Second.png")

# with open("ProjectsWithPython/QRCODES/first.png") as f:
#     f.write(image)