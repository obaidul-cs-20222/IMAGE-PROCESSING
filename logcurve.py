#log curve with two different c values

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,256,0.1)
c=np.arange(0.00023,1,0.00023)
for i in range (2):
    print(c[i])
    y=c[i]*np.log(x+1)
    plt.plot(x,y)

plt.title("log curve with var c")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
    
