import cv2
import numpy as np
im=cv2.imread('ff.jpg')
cv2.imshow('imagedisplay',im)
h,w,c=im.shape

print(im.dtype)

rim=np.zeros([h,w,3])
gim=np.zeros([h,w,3])
bim=np.zeros([h,w,3])

for i in range (h):
    for j in range(w):
            rim[i][j][2]=im[i][j][2]
            gim[i][j][1]=im[i][j][1]
            bim[i][j][0]=im[i][j][0]


            

rim = rim.astype(np.uint8)
gim = gim.astype(np.uint8)
bim = bim.astype(np.uint8)
        

cv2.imshow('greenImage',gim)
cv2.imshow('blueImage',bim)
cv2.imshow('redImage',rim)
