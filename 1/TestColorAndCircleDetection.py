import cv2
import numpy as np

#Find the picture, resize it and to show it
img = cv2.imread('Images\Blackball2.png')
img = cv2.resize(img, (600,400))
cv2.imshow('image', img)

#Color Detection for the white color
lowerwhite = np.array([0, 0, 240])
upperwhite = np.array([180, 90, 255])
imagewhite = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskwhite = cv2.inRange(imagewhite, lowerwhite, upperwhite)
#cv2.imshow('Treated Image White', imagewhite)
cv2.imshow('Mask White', maskwhite)

#Color Detection for the red color
lowerred = np.array([160, 50, 80])
upperred = np.array([180, 255, 255])
imagered = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
maskred = cv2.inRange(imagered, lowerred, upperred)
#cv2.imshow('Treated Image Red', imagered)
cv2.imshow('Mask Red', maskred)

#Color Detection for the yellow color
loweryellow = np.array([20, 50, 200])
upperyellow = np.array([40, 255,255])
imageyellow = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskyellow = cv2.inRange(imageyellow, loweryellow, upperyellow)
#cv2.imshow('Treated Image Yellow', imageyellow)
cv2.imshow('Mask Yellow', maskyellow)

#Color Detection for the blakc holes
lowerhole = np.array([0, 0, 0])
upperhole = np.array([180, 255, 40])
imagehole = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskhole = cv2.inRange(imagehole, lowerhole, upperhole)
#cv2.imshow('Treated Image Hole', imagehole)
cv2.imshow('Mask Hole', maskhole)

#To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
