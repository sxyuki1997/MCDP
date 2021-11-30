import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (6,5)


s = [0,0.5,1,2,3,4]

pl = [2.5, 3.958, 4.945, 7.74,  19.205, 68.295]

plt.plot(s,pl,marker='o')
plt.xlabel("位置关联强度 $s^2$")
plt.ylabel("$max(MCDPL)$")
plt.title("位置关联强度与max(MCDPL)")
plt.show()