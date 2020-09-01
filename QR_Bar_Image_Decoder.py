# Decoding QR from images using OpenCV
# author - rudrajit1729

# Importing Libraries
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Read & decode images
img = cv2.imread('ID.png')
code = decode(img)

# Display Content
# print(code)
for barcode in code:
	data = barcode.data.decode('utf-8')
	print("The data : {}\nThe position : {}\n".format(data, barcode.rect))

