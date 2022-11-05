import cv2
import numpy as np
import matplotlib.pyplot as plt

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
#in here we will specify our region of interest
# we will make our mask with black pixels and then specify our region of interest then we will fill them together
def region_of_interest(image):
    height=image.shape[0]
    triangles=np.array([
        [(200,height),(1100,height),(550,250)]
    ])
    mask=np.zeros_like(image)
#it takes an array of traingles not only one
    cv2.fillPoly(mask ,triangles, 255)
    return mask   

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny=canny(lane_image)


#it waits time for the image to be displayed
#0 makes the image run infinitely until we press any key

cv2.imshow("image",region_of_interest(canny))
cv2.waitKey(0)

#note
# we used plt to display the image in a better way so we can get our region of interest in x,y