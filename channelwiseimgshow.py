import cv2
import numpy as np
im=cv2.imread('dd.jpg')
cv2.imshow('imagedisplay',im)
h,w,c=im.shape

print(im.dtype)

rim=np.zeros([h,w])
gim=np.zeros([h,w])
bim=np.zeros([h,w])

for i in range (h):
    for j in range(w):
        rim[i][j]=im[i][j][2]

for i in range (h):
    for j in range(w):
        gim[i][j]=im[i][j][1]

for i in range (h):
    for j in range(w):
        bim[i][j]=im[i][j][0]

rim = rim.astype(np.uint8)
gim = gim.astype(np.uint8)
bim = bim.astype(np.uint8)

cv2.imshow('greenImage',gim)
cv2.imshow('blueImage',bim)
cv2.imshow('redImage',rim)
