import qrcode
make = qrcode.make("https://www.python.org/")
make.save("PicofQR.png")
