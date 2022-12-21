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
gray_blurred = cv2.blur(gray, (3, 3))
cv2.imshow("Treated Image Gray Blurred", gray_blurred)
  
# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 5, param1 = 50,
               param2 = 10, minRadius = 1, maxRadius = 100)
  
# Draw circles that are detected.
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

cv2.imshow("Detected circles on the image", detected_circles)

# To exit all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()