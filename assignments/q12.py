#  Write a program to read two images ‘lena.bin’ and peppers.bin’. define a new 256 x 256 image J as follows : the left 
#half of J i.e., the first 128 columns, should be equal to the left half of lena image and the right half of J, i.e., the 129th 
#column through the 256th column should be equal to the right half of pepper image. Show J image. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    img1=cv2.imread('ff.jpg',0)
    img2=cv2.imread('bb.jpg',0)
    img1=cv2.resize(img1,(256,256))
    img2=cv2.resize(img2,(256,256))
    combined_image=np.zeros([256,256]).astype(np.uint8)
    for i in range(256):
        for j in range(256):
            if j<=127:
                combined_image[i,j]=img1[i,j]
            else:
                combined_image[i,j]=img2[i,j]
    
    fig = plt.figure(figsize=(18, 18))
    pltX = 1
    pltY = 3

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("FIRST IMAGE")
    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title("SECOND IMAGE")
    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(combined_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title("COMBINED IMAGE")
    fig.show()
    fig.waitforbuttonpress()
    

main()
    
