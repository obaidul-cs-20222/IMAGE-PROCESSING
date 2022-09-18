import cv2
im=cv2.imread('dd.jpg')
cv2.imshow('imagedisplay',im)
print("shape of the image is",end=" ")
print(im.shape)
h,w,c=im.shape
print(h,w,c)
print(im)
cv2.waitKey(0)

