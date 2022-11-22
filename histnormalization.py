import numpy as np
import cv2
import matplotlib.pyplot as plt

def normalizehist(hist):
    normhist=np.zeros(256,dtype="float")
    for i in range(256):
        normhist[i]=hist[i]/sum(hist)
    return normhist


def perforequalization(nhist):
    cumfreq=np.zeros(256,dtype="float")
    lookuptable=np.zeros(256,dtype="float")
    cumfreq[0]=nhist[0]
    for i in range(1,256):
        cumfreq[i]=cumfreq[i-1]+nhist[i]

    for i in range(256):
        lookuptable[i]=np.round(cumfreq[i]*i)
    return lookuptable

def findhistogram(img):
    h,w=img.shape
    hist=np.zeros(256,dtype='uint32')
    for i in range(h):
        for j in range(w):
            hist[img[i,j]]+=1
    return hist


img=cv2.imread('bb.jpg',0)
h,w=img.shape
hist=findhistogram(img)
#plt.plot(hist)
#plt.show()

nhist=normalizehist(hist)
#plt.plot(nhist)
#plt.show()

lookuptable=perforequalization(nhist)
eqim=img

for i in range(h):
    for j in range(w):
        eqim[i,j]=lookuptable[img[i,j]]
#cv2.imshow("original",img)
#cv2.imshow("equalized",eqim)
#cv2.waitKey(0)
newhist=findhistogram(eqim)
#hist=findhistogram(newhist)
plt.plot(hist)
plt.show()

fig, axs=plt.subplots(5,1)

axs[0].plot(hist)
axs[0].set_title('Axis [0, 0]')
axs[1].plot(nhist)
axs[1].set_title('grey scale')
axs[2].imshow(img,cmap="gray")
axs[2].set_title('Axis [1, 0]')

axs[3].imshow(eqim,cmap="gray")
axs[3].set_title('Axis [0, 0]')
axs[4].plot(newhist)
axs[4].set_title('Axis [0, 1]')
plt.waitforbuttonpress()
