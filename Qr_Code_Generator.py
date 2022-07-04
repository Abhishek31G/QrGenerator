import pyqrcode

text = input("Enter the text you want to convert it in a Qr Code? ")
qr_code = pyqrcode.create(text)
qr_code.svg("qr_code.svg", module_color='#000', background='#FFF', scale=12)


