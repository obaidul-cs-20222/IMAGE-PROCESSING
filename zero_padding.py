import cv2
import numpy as np
import matplotlib.pyplot as plt

def zeropadding(img):# padding for color image
    h,w,c=img.shape
    newimg=np.zeros([h+2,w+2,c]).astype(np.uint8)
    for i in range (h):
        for j in range(w):
            newimg[i+1,j+1,0]=img[i,j,0]
            newimg[i+1,j+1,1]=img[i,j,1]
            newimg[i+1,j+1,2]=img[i,j,2]
    return newimg


def zeropaddingbw(img):#padding for gray scale image
    h,w=img.shape
    newimg=np.zeros([h+2,w+2]).astype(np.uint8)
    for i in range (h):
        for j in range(w):
            newimg[i+1,j+1]=img[i,j]
    return newimg




im=cv2.imread('bb.jpg',1)

fig = plt.figure(figsize=(18, 18))
pltX = 1
pltY = 3

fig.add_subplot(pltX, pltY, 1)
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("Original Image")
newimage=zeropadding(im)
fig.add_subplot(pltX, pltY, 2)
plt.imshow(cv2.cvtColor(newimage,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title("image with zero padding")
im=cv2.imread('bb.jpg',0)
newimage=zeropaddingbw(im)
fig.add_subplot(pltX, pltY, 3)
plt.imshow(cv2.cvtColor(newimage,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title("black and white image with zero padding")
fig.show()
fig.waitforbuttonpress()

print(im.shape)
print(newimage.shape)

