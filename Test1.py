import numpy as np
import matplotlib.pyplot as plt
 
# Dataset
gamma=np.arange(0, 1, .1)
c=1.5
x = np.arange(0,256,0.1)  # start,stop,step
print(x)

for i in range(len(gamma)):
    y = c*x**gamma[i]
    # Plotting the Graph
    plt.plot(x, y)
    
plt.title("Log Curve with varying C")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
