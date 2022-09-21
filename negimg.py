import cv2 
import numpy as np
import matplotlib.pyplot as plt
def negim(im):
    h,w=im.shape
    newIm=np.zeros([h,w]).astype(np.uint8)
   
    for i in range(h):
        for j in range(w):
            newIm[i][j]=255-im[i][j]
    return(newIm)




im=cv2.imread('6.jpg',0)
im1=negim(im)
#cv2.imshow('image',im1)

fig, axs=plt.subplots(2)

axs[0].imshow(im)
axs[0].set_title('RGB IMAGE')
axs[1].imshow(im1)    
axs[1].set_title('negative IMAGE')
plt.waitforbuttonpress()
