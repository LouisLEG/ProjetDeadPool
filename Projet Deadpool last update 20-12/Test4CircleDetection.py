import cv2
import numpy as np

# Find the picture and resize it
img = cv2.imread('Images\Blackball1.png')
img = cv2.resize(img, (600,300))
#cv2.imshow("Original Image", img)

# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
#cv2.imshow("Gray Blurred Image", gray)

# Detecting circles 
rows = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=10, minRadius=5, maxRadius=15)
circles = np.uint16(np.around(circles))

# Showing circles detected
for i in circles[0,:]:
    cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img, (i[0],i[1]),2,(0,0,255),2)
cv2.imshow('Circle Detection', img)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
