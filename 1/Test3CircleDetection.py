import cv2
import numpy as np

#Find the picture and resize it
img = cv2.imread('Images\Blackball2.png')
img = cv2.resize(img, (600,400))
cv2.imshow("Original Image", img)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Treated Image Gray", gray)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (5, 5))
cv2.imshow("Treated Image Gray Blurred", gray_blurred)

# Hough_Circles 
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 10, param1=180, param2=60  , minRadius=0, maxRadius=400)
detected_circles = np.uint16(np.around(detected_circles))

# Drawing the circles and its center
for i in detected_circles[0,:]:
    cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)

# Showing the detected circles
cv2.imshow('Detected Circles', gray)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()