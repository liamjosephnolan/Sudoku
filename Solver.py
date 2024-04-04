import cv2
import numpy as np

print("Program Running....")


img = cv2.imread('test_images/real_test1.jpg',0)

cv2.imshow('Image',img)

cv2.waitKey(0)

img = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow('Image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()




