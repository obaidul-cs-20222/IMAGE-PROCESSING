import cv2
import numpy as np
im=cv2.imread('6.jpg',1)
#cv2.imshow('display',im)
#print(im.shape)
#print(im)
h,w,c=im.shape
nim=np.zeros([h,w])
for i in range(h):
    for j in range(w):
        nim[i][j]=164-im[i][j][2]
# print(h,w)
cv2.imshow('new',nim)

cv2.waitKey(0)
cv2.destroyAllWindows()