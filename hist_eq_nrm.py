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


nhist=normalizehist(hist)


lookuptable=perforequalization(nhist)
eqim=img

for i in range(h):
    for j in range(w):
        eqim[i,j]=lookuptable[img[i,j]]

newhist=findhistogram(eqim)

fig, axs=plt.subplots(4,1)

axs[1].plot(hist)
axs[1].set_title('HISTOGRAM FOR ORIGINAL IMAGE')
axs[0].imshow(img,cmap="gray")
axs[0].set_title('ORIGINAL IMAGE')
axs[2].imshow(eqim,cmap="gray")
axs[2].set_title('EQUALIZED IMAGE')
axs[3].plot(newhist)
axs[3].set_title('EQUALIZED HISTOGRAM')
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=1,hspace=0.4)
plt.waitforbuttonpress()
