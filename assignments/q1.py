#Write a program to do image format conversion i.e., from RGB to gray, gray to binary, RGB to binary
import numpy as np
import matplotlib.pyplot as plt
import cv2

def extraction(img):
    h,w,chan=img.shape
    red=np.zeros([h,w],dtype=np.uint8)
    green=red
    blue=red
    
    for i in range (h):
        for j in range(w):
            red[i,j]=img[i,j,2]
            green[i,j]=img[i,j,1]
            blue[i,j]=img[i,j,0]
    return red,green,blue

def gray_conversion(red,green,blue):
    h,w=red.shape
    gray_image=np.zeros([h,w],dtype=np.uint8)
    
    for i in range(h):
        for j in range(w):
            gray_image[i,j]=red[i,j]*0.3+green[i,j]*0.59+blue[i,j]*0.11
    return gray_image

def gray_to_binary(img):
    binary_img=img
    a=int(input("enter the threshhold value: "))
    h,w=img.shape
    for i in range(h):
        for j in range(w):
            if img[i][j]>a:
                binary_img[i][j]=255
            else:
                binary_img[i][j]=0
    return binary_img
    


def main():
    img=cv2.imread('ff.jpg',1)
    r,g,b=extraction(img)
    gray_image=gray_conversion(r,g,b)

    fig = plt.figure(figsize=(18, 18))
    pltX = 1
    pltY = 4
    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title(" ORIGINAL IMAGE ")
    
    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(gray_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" GRAY SCALE IMAGE ")

    binary_image=gray_to_binary(gray_image)
    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(binary_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" GRAY SCALE IMAGE TO BINARY IMAGE ")
    bin1=gray_to_binary(gray_image)
    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(binary_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" RGB IMAGE TO BINARY IMAGE ")
    fig.show()
    fig.waitforbuttonpress()

main()


    

