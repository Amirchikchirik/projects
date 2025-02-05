import segno

qr = segno.make_qr(input("ссылка: "))

qr.save("qr.png", scale=10)

