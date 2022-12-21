import cv2
import numpy as np

# Find the picture and resize it
img = cv2.imread('Images\Blackball11.png')
img = cv2.resize(img, (600,300))
cv2.imshow("Original Image", img)

# Remove the background to have only the balls


# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

# Detecting circles 
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,25, param1=100, param2=11, minRadius=2, maxRadius=10)
circles = np.uint16(np.around(circles))

# Showing circles detected
for i in circles[0,:]:
    cv2.circle(img, (i[0],i[1]),i[2],(0,255,0),1)
    cv2.circle(img, (i[0],i[1]),2,(0,0,255),1)
cv2.imshow('Circle Detection', img)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
