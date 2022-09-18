import cv2
import numpy as np

def grey(im):
    h,w,c=im.shape
    gim=np.zeros([h,w])
    gim=gim.astype(np.uint8)
    for i in range(h):
        for j in range(w):
            #gim[i][j]=((im[i][j][0]+im[i][j][1]+im[i][j][2])//3) sum er value ubyte er range i.e 255 er baire
            #chole jachhe tai int e typecast kora. otherwise it will give an error as follows:RuntimeWarning: overflow encountered in ubyte_scalars
            gim[i][j]=((int(im[i][j][0])+int (im[i][j][1])+int(im[i][j][2]))//3)
    return gim


im=cv2.imread('dd.jpg')
cv2.imshow('imagedisplay',im)
ans=grey(im)
cv2.imshow('imagedisplay',ans)
cv2.waitKey(0)