# imports
import cv2

# import flower image
image = cv2.imread('../Assets/flower.jpg')

# show image 
cv2.imshow('flower',image)

# show image in grayscale
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('flower_grayscale',image)

# write image
cv2.imwrite('../Assets/edges_flower.jpg',cv2.Canny(image,200,300))

# show img after detecting edges
cv2.imshow('edges_flower', cv2.imread('../Assets/edges_flower.jpg'))

# wait for user to exit
cv2.waitKey(0)

# import dolphin img
image = cv2.imread('../Assets/dolphin.jpg')

# show image 
cv2.imshow('flower',image)

# show image in grayscale
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('dolphin_grayscale',image)

# write img
cv2.imwrite('../Assets/edges_dolphin.jpg',cv2.Canny(image,200,300))

# show img after detecting edges
cv2.imshow('edges_dolphin', cv2.imread('../Assets/edges_dolphin.jpg'))

# wait for user to exit
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()