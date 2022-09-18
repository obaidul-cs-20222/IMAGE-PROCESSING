import cv2
im=cv2.imread('untitled.bmp')
cv2.imshow('imagedisplay',im)
#print(im.shape)
h,w,c=im.shape
h1=h//2
h2=h1-10
w1=w//2
w2=w1+10

print(im[h1][w1][0],im[h1][w1][1],im[h1][w1][2])
print(im[h2][w2][0],im[h2][w2][1],im[h2][w2][2])
cv2.waitKey(0)
