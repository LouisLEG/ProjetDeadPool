import cv2
import numpy as np

# Test avec Threshold 

# Find the picture and resize it
img = cv2.imread('Images\Blackball00.png', 0)
img = cv2.resize(img, (600,300))
cv2.imshow('Original Image', img)

# Find the background picture and resize it
background = cv2.imread('Images\Blackball000.png',0 )
background = cv2.resize(background, (600,300))
cv2.imshow('Background Image', background)

# Treatment of images
iwb = cv2.subtract(img, background)
cv2.imshow('Image Without Background', iwb)

# Treatment of the image without background
grayiwb = cv2.cvtColor(iwb, cv2.COLOR_BGR2GRAY)
grayiwbb = cv2.medianBlur(grayiwb, 7)
cv2.imshow('Blurred Image Without Background', grayiwbb)
'''
# Detection circles 
circles = cv2.HoughCircles(grayiwbb, cv2.HOUGH_GRADIENT, 1,25, param1=100, param2=11, minRadius=1, maxRadius=20)
circles = np.uint16(np.around(circles))

# Showing circles detected
for i in circles[0,:]:
    cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img, (i[0],i[1]),2,(0,0,255),3)
cv2.imshow('Circle Detection', img)
'''
# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
