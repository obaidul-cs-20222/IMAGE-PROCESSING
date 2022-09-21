import cv2
import numpy as np
import matplotlib.pyplot as plt
im=cv2.imread('dd.jpg')
#cv2.imshow('imagedisplay',im)
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


fig, axs=plt.subplots(1,4)

axs[0].imshow(rim,cmap='gray')
axs[0].set_title('RED IMAGE')
axs[1].imshow(gim,cmap='gray')
axs[1].set_title('GREEN IMAGE')
axs[2].imshow(bim,cmap='gray')
axs[2].set_title('BLUE IMAGE')
axs[3].imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
axs[3].set_title('ACTUAL IMAGE')
plt.waitforbuttonpress()
cv2.imshow('greenImage',gim)
cv2.imshow('blueImage',bim)
cv2.imshow('redImage',rim)
cv2.waitKey()
