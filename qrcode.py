import segno

qr = segno.make_qr(input("link: "))

qr.save("qr.png", scale=10)

