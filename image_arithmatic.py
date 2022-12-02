import cv2

import numpy as np

import matplotlib.pyplot as plt


def channelExtraction(img):

    row, col, chan = img.shape
    Rchan = np.zeros((row, col), dtype=np.uint8)
    Gchan = np.zeros((row, col), dtype=np.uint8)
    Bchan = np.zeros((row, col), dtype=np.uint8)

    m = 0
    for i in img:
        n = 0
        for j in i:
            r, g, b = j
            Rchan[m, n] = r
            Gchan[m, n] = g
            Bchan[m, n] = b
            n = n+1
        m = m+1

    return Bchan, Gchan, Rchan


def grayConversion(B, G, R):

    row, col = B.shape
    gray_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            gray_chan[i, j] = R[i, j]*0.3 + G[i, j]*0.59 + B[i, j]*0.11

    return gray_chan


def imageAddition(grayImg1,grayImg2):

    row,col = grayImg1.shape

    imgAdd = np.zeros((row,col), dtype=np.float32)

    for i in range(row):

        for j in range(col):

            imgAdd[i,j] = int(grayImg1[i,j]) +int( grayImg2[i,j])
            
    
    return imageNormalisation(imgAdd)

def imageSubtraction(grayImg1,grayImg2):

    row,col = grayImg1.shape

    imgSub = np.zeros((row,col), dtype=np.float32)

    for i in range(row):

        for j in range(col):

            imgSub[i,j] = int(grayImg1[i,j]) - int( grayImg2[i,j])

    return imageNormalisation(imgSub)

def imageMultiplication(grayImg1,grayImg2):

    row,col = grayImg1.shape

    imgMul = np.zeros((row,col), dtype=np.float32)

    for i in range(row):

        for j in range(col):

            imgMul[i,j] = int(grayImg1[i,j]) * int(grayImg2[i,j])

    return imageNormalisation(imgMul)

def imageDivision(grayImg1,grayImg2):

    row,col = grayImg1.shape

    imgDiv = np.zeros((row,col), dtype=np.float32)

    for i in range(row):

        for j in range(col):
            if grayImg1[i,j]>0:
                imgDiv[i,j] = int (grayImg2[i,j]) // int(grayImg1[i,j])
            elif grayImg2[i,j]>0:
                imgDiv[i,j] = int (grayImg1[i,j]) // int(grayImg2[i,j])
            else:
                imgDiv[i,j] = int (grayImg1[i,j]) // int(grayImg2[i,j])



    return imageNormalisation(imgDiv)

def imageNormalisation(img):

    row,col = img.shape

    normalisedImg = np.zeros((row,col), dtype=np.uint8)

    min_pixel = np.min(img)

    max_pixel = np.max(img)

    for  i in range(row):

        for j in range(col):

            normalisedImg[i,j] = (255*(img[i,j] - min_pixel)/(max_pixel - min_pixel)).astype(int)             

    return normalisedImg


if __name__ == "__main__":

    img1 = cv2.imread("bb.jpg")

    img2 = cv2.imread("ff.jpg")

    B1, G1, R1 = channelExtraction(img1)

    B2, G2, R2 = channelExtraction(img2)

    grayImg1 = grayConversion(B1, G1, R1)

    grayImg2 = grayConversion(B2, G2, R2)

    imgAdd = imageAddition(grayImg1,grayImg2)

    imgSub = imageSubtraction(grayImg1,grayImg2)

    imgMul = imageMultiplication(grayImg1,grayImg2)

    imgDiv = imageDivision(grayImg1,grayImg2)

    print(imgDiv)

    
    fig = plt.figure(figsize=(30, 18))
    pltX = 3
    pltY = 2

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(grayImg1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image 1")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(grayImg2, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image 2")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(imgAdd, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Addition")

    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(imgSub, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Subtraction")

    fig.add_subplot(pltX, pltY, 5)
    plt.imshow(cv2.cvtColor(imgMul, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Multiplication")

    fig.add_subplot(pltX, pltY, 6)
    plt.imshow(cv2.cvtColor(imgDiv, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Division")
                             
    fig.show()
    fig.waitforbuttonpress()
