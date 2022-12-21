import cv2
import numpy as np

# Find the picture and resize it
img = cv2.imread('Images\Blackball11.png')
img = cv2.resize(img, (600,300))
cv2.imshow("Original Image", img)

# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

# Detecting lines
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

# Drawing lines detected
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)
cv2.imshow('image', img)

# To exit all the windows
k = cv2.waitKey(0)
cv2.destroyAllWindows()