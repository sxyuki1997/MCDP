import numpy as np
import matplotlib.pyplot as plt

x = [i*0.01 for i in range(1,100)]
y = []

for i in x:
    y.append((i-1)/(1+i) * (i / np.log(i)))


plt.plot(x,y)
plt.show()