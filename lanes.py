import cv2
import numpy as np
#we are using canny functions
image=cv2.imread('test_image.jpg')
#first step is to convert the image to a gray scale image
lane_image=np.copy(image)
gray_image=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
#second step is to applying gaussian blur on the image
#we do that to reduce noise in our image because it can make false edges
#this wil apply a gaussian blur filter with size 5x5 with deviation 0 on the gray image
blur=cv2.GaussianBlur(gray_image,(5,5),0)

#it waits time for the image to be displayed
#0 makes the image run infinitely until we press any key

cv2.imshow("image",gray_image)
cv2.waitKey(0)