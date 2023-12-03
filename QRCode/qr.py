import qrcode

text = input("Enter the text: ")
name = input("Enter the file name (without .png extension): ")
img = qrcode.make(text)
filename = name + ".png"
img.save(filename)