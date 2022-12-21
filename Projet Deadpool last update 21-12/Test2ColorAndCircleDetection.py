import cv2
import numpy as np

# Find the picture and resize it
imgo = cv2.imread('Images\Blackball0.png')
imgo = cv2.resize(imgo, (600,300))
cv2.imshow("Original Image", imgo)
"""
# Convert to gray scale
grayo = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY)
grayo = cv2.medianBlur(grayo, 5)
cv2.imshow("Gray Blurred Image", grayo)

# Detecting circles 
rows = grayo.shape[0]
circles = cv2.HoughCircles(grayo, cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=100, param2=10, minRadius=10, maxRadius=15)
circles = np.uint16(np.around(circles))

# Showing circles detected
for i in circles[0,:]:
    cv2.circle(imgo, (i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(imgo, (i[0],i[1]),2,(0,0,255),2)
cv2.imshow('Circle Detection O', imgo)
"""
# Find the picture and resize it
img = cv2.imread('Images\Blackball3.png')
img = cv2.resize(img, (600,300))
cv2.imshow('Original image', img)

# Colors Detection
lowerwhite = np.array([29, 25, 180])
upperwhite = np.array([51, 79, 255])
imagewhite = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskwhite = cv2.inRange(imagewhite, lowerwhite, upperwhite)

lowerred = np.array([114, 47, 34])
upperred = np.array([179, 255, 255])
imagered = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
maskred = cv2.inRange(imagered, lowerred, upperred)

loweryellow = np.array([16, 82, 95])
upperyellow = np.array([71, 255,255])
imageyellow = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskyellow = cv2.inRange(imageyellow, loweryellow, upperyellow)

lowerhole = np.array([0, 0, 0])
upperhole = np.array([179, 255, 27])
imagehole = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
maskhole = cv2.inRange(imagehole, lowerhole, upperhole)

output = np.zeros_like(maskred)
allmasks = output + maskred + maskyellow + maskwhite + maskhole
cv2.imshow('All masks together', allmasks)

# Circles Detection
gray = cv2.medianBlur(allmasks, 5)
rows = allmasks.shape[0]
circles = cv2.HoughCircles(allmasks, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=10, minRadius=5, maxRadius=15)
circles = np.uint16(np.around(circles))

# Showing circles detected
for i in circles[0,:]:
    cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img, (i[0],i[1]),2,(0,0,255),2)
cv2.imshow('Circle Detection', img)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
