import cv2

image=cv2.imread('test_image.jpg')
cv2.imshow("image",image)
#it waits time for the image to be displayed
#0 makes the image run infinitely until we press any key
cv2.waitKey(0)