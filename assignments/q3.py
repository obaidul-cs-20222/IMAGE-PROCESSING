import numpy as np
import matplotlib.pyplot as plt
import cv2

import cv2
import numpy as np
import matplotlib.pyplot as plt
im=cv2.imread('ff.jpg')
h,w,c=im.shape

rim=np.zeros([h,w,3])
gim=np.zeros([h,w,3])
bim=np.zeros([h,w,3])

for i in range (h):
    for j in range(w):
        for k in range(3):
            rim[i][j][k]=im[i][j][2]
            gim[i][j][k]=im[i][j][1]
            bim[i][j][k]=im[i][j][0]

        
rim = rim.astype(np.uint8)
gim = gim.astype(np.uint8)
bim = bim.astype(np.uint8)
        
fig = plt.figure(figsize=(18, 18))
pltX = 1
pltY = 4
fig.add_subplot(pltX, pltY, 1)
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title(" ORIGINAL IMAGE ")
    
fig.add_subplot(pltX, pltY, 2)
plt.imshow(cv2.cvtColor(rim,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" RED CHANNEL IMAGE ")
fig.add_subplot(pltX, pltY, 3)
plt.imshow(cv2.cvtColor(gim,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" GREEN CHANNEL IMAGE ")
fig.add_subplot(pltX, pltY, 4)
plt.imshow(cv2.cvtColor(bim,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" BLUE CHANNEL IMAGE ")
fig.show()
fig.waitforbuttonpress()
