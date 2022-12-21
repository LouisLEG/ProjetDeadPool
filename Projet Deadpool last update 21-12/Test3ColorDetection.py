import cv2
import numpy as np

# Find the picture and resize it
img = cv2.imread('Images\Blackball2.png')
img = cv2.resize(img, (600,300))
cv2.imshow('Original image', img)

# Color Detection for the white color
lowerwhite = np.array([29, 25, 180])
upperwhite = np.array([51, 79, 255])
imagewhite = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskwhite = cv2.inRange(imagewhite, lowerwhite, upperwhite)
#cv2.imshow('Treated Image White', imagewhite)
cv2.imshow('Mask White', maskwhite)

# Color Detection for the red color
lowerred = np.array([114, 47, 34])
upperred = np.array([179, 255, 255])
imagered = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
maskred = cv2.inRange(imagered, lowerred, upperred)
#cv2.imshow('Treated Image Red', imagered)
cv2.imshow('Mask Red', maskred)

# Color Detection for the yellow color
loweryellow = np.array([16, 82, 95])
upperyellow = np.array([71, 255,255])
imageyellow = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskyellow = cv2.inRange(imageyellow, loweryellow, upperyellow)
#cv2.imshow('Treated Image Yellow', imageyellow)
cv2.imshow('Mask Yellow', maskyellow)

# Color Detection for the black holes
lowerhole = np.array([0, 0, 0])
upperhole = np.array([179, 255, 27])
imagehole = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskhole = cv2.inRange(imagehole, lowerhole, upperhole)
#cv2.imshow('Treated Image Hole', imagehole)
cv2.imshow('Mask Hole', maskhole)

# Reassembly all the masks together
output = np.zeros_like(maskred)
output = output + maskred + maskyellow + maskwhite + maskhole
cv2.imshow('All masks together', output)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
