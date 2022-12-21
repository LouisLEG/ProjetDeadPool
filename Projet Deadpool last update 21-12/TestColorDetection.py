import cv2
import numpy as np

# Find the picture and resize it
img = cv2.imread('Images\Blackball1.png')
img = cv2.resize(img, (600,300))

# Color Detection for the white color
lowerwhite = np.array([0, 0, 190])
upperwhite = np.array([180, 50, 255])
imagewhite = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
maskwhite = cv2.inRange(imagewhite, lowerwhite, upperwhite)
cv2.imshow('maskwhite', maskwhite)

# Color Detection for the red color
lowerred = np.array([160, 50, 200])
upperred = np.array([180, 255, 255])
imagered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskred = cv2.inRange(imagered, lowerred, upperred)
cv2.imshow('maskred', maskred)

# Color Detection for the yellow color
loweryellow = np.array([20, 50, 200])
upperyellow = np.array([40, 255, 255])
imageyellow = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskyellow = cv2.inRange(imageyellow, loweryellow, upperyellow)
cv2.imshow('maskyellow', maskyellow)

# To show the initial picture
cv2.imshow('image', img)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
