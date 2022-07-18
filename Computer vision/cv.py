# imports
import cv2
import numpy as np

# import flower image
image = cv2.imread('../Assets/flower.jpg')

# show image
cv2.imshow('flower',image)

# destroy window
cv2.destroyWindow('flower')

# write image
cv2.imwrite('../Assets/flower.jpg',image)

# import dolphin img
image = cv2.imread('../Assets/dolphin.jpg')

# show img
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('dolphin',image)

# write img
cv2.imwrite('edges_dolphin.jpg',cv2.Canny(image,200,300))

# show img after write
cv2.imshow('edges', cv2.imread('edges_dolphin.jpg'))