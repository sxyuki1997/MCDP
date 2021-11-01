import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 600
plt.rcParams['figure.figsize'] = (6,5)

x = [i*0.01 for i in range(100)]

y = []
for i in x:
    if i == 0:
        y.append(0)
    else:
        y.append(-i*np.log2(i)-(1-i)*np.log2(1-i))

x.append(1)
y.append(0)

plt.plot(x,y)
plt.xlabel("p(x)")
plt.ylabel("H(X)")
plt.grid()
plt.title("信息熵与事件发生概率")
plt.savefig('../img/entropy.png')
plt.show()

