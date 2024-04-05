import cv2
import numpy as np

print("Program Running....")

img = cv2.imread('test_images/real_test1.jpg', 0)
cv2.imshow('Image', img)
cv2.waitKey(0)

img = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Image', img)
cv2.waitKey(0)

# Lower the thresholds for Canny edge detection
edges = cv2.Canny(img, 30, 90)  # Adjust these values as needed

# Dilate the edges to connect the lines
kernel = np.ones((3,3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# Find contours
contours, hierarchy = cv2.findContours(dilated_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if contours is not None:
        cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

        cv2.imshow('Image', img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

