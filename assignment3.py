#RUNS PERFECTLY
import cv2
import matplotlib.pyplot as plt 
import numpy as np
def stretchandsqueeze(img):
    a=int(input("enter the value of a: "))
    b=int(input("enter the value of b: "))
    n,m=0,255
    h,w=im.shape
    for i in range(h):
        for j in range(w):
            if img[i][j]<m:
                m=img[i][j]
            if img[i][j]>n:
                n=img[i][j]
    print(n,m)
    r=(b-a)/(n-m)
    newimage=np.zeros([h,w]).astype(np.uint8)
    
    for i in range (h):
        for j in range(w):
            newimage[i][j]=a+r*img[i][j]
    return newimage



im=cv2.imread('bb.jpg',0)
newimg=stretchandsqueeze(im)
newimage=stretchandsqueeze(newimg)
fig = plt.figure(figsize=(18, 18))
pltX = 1
pltY = 3
fig.add_subplot(pltX, pltY, 1)
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("ORIGINAL IMAGE")

fig.add_subplot(pltX, pltY, 2)
plt.imshow(cv2.cvtColor(newimg,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("SQUEEZED IMAGE")
fig.add_subplot(pltX, pltY, 3)
plt.imshow(cv2.cvtColor(newimage,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("STRETCHED IMAGE")
plt.show
plt.waitforbuttonpress()


