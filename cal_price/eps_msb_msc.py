import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cal_price import utility

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (6,5)

# laplace加噪
def _lapalce_mech(e):
    beta = 1 / e
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 < 0.5:
        noise = int(beta * np.log(2 * u2))
    else:
        noise = int(-beta * np.log(2 - 2 * u2))
    return noise

data = 100

ACC = []
eps = [i*0.01 for i in range(1,600)]
for e in eps:
    acc = 1 - 1/np.e**(0.9*e)
    ACC.append(acc)

plt.plot(eps, ACC)
plt.xlabel("隐私保护参数 $\epsilon$")
plt.ylabel("数据精度")
plt.grid()
plt.title("边际社会效益估计曲线")
plt.show()

print(1 - 1/np.e**(0.9*3))