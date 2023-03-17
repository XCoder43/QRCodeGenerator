import qrcode as qr

qrName = input("Enter The Link/Output Of Your QR Code: ")
fName = input("Enter Your File Name: ")

img = qr.make(qrName)
img.save(fName + ".png")