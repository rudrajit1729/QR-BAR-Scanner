# Live QR and Bar Code Scanner
# author - rudrajit1729
# Importing Libraries
import numpy as np
import cv2
from pyzbar.pyzbar import decode

# Capture
cap = cv2.VideoCapture(0) # Webcam
# Setting width and height
# id for width = 3, height = 4 
# Set width to ___ and height to ___ acc to project
cap.set(3, 640)
cap.set(4, 480)
while True:
	# Read and decode
	success, img = cap.read()
	for code in decode(img):
		data = code.data.decode('utf-8')
		print(data)
		# Surround with polygon
		# Convert to numpy array and reshape
		pts = np.array([code.polygon], np.int32)
		pts = pts.reshape((-1, 1, 2))
		# Draw line - params(img, array, isClosed, col, thickness)
		cv2.polylines(img, [pts], True, (255, 0, 255), 5)
		toppts = code.rect
		# Write the info - params(img, text, font, scale, col, thickness)
		# Show the text on screen
		cv2.putText(img, data, (toppts[0], toppts[1]), 
			cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

	# Show updated img on screen
	cv2.imshow('Result', img)
	cv2.waitKey(1)
	
