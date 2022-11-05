import cv2
import numpy as np

#first step is to convert the image to a gray scale image

#second step is to applying gaussian blur on the image
#we do that to reduce noise in our image because it can make false edges
#this wil apply a gaussian blur filter with size 5x5 with deviation 0 on the gray image

#the last step is an optional step because we will ue canny algorithm in which it uses gaussian filter already
#as we know we can describe our image using a matrix of pixels
#then how canny algorithm is working ?
#we will take derivative of each pixels and its neighbors 
#if the value between them is high then it's an edge , if not the it's not an edge
#just take care that derivative is that we will subtract each pixel from it's neighbors
#so the pixels of the same color will be black and the edges only will be white
#if the edge pixel is below low_threshold then it's rejected
#if it's higher than high_threshold then it's accepted
#if it's in between so it wil be accepted only in case it's connected to a strong edge
def canny(image):
    gray_image = cv2.cvtColor (image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray_image,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny=canny(lane_image)


#it waits time for the image to be displayed
#0 makes the image run infinitely until we press any key

cv2.imshow("image",canny)

cv2.waitKey(0)