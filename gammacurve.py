import numpy as np
import matplotlib.pyplot as plt
fig, axs=plt.subplots(1,2)
gamma=np.arange(0.11,0.20,0.05)
x=np.arange(1,100,5)
c=1.5

for i in range(2):
    y=c*x**gamma[i]
    axs[0].plot(x,y)
    axs[0].set_title('gamma curve')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')


gamma=1
x=np.arange(1,100,5)
c=np.arange(1,10,2)
for i in range(2):
    y=c[i]*x**gamma
    axs[1].plot(x,y)
    axs[1].set_title('gamma curve with two different c values and fixed gamma value')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('y')

plt.show()


