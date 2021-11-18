import numpy as np
import matplotlib.pyplot as plt
import time

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(6, 5))

eps = 3.25


bpl = [3.25, 4.71, 4.74, 4.74, 4.74, 4.74, 4.74, 4.74, 4.74, 4.74, 4.74, 4.74]
fpl = [5.12, 5.12, 5.12, 5.12, 5.12, 5.12, 5.12, 5.12, 5.12, 5.12, 5.07, 3.25]
tpl = []
for i in range(len(bpl)):
    tpl.append(round(bpl[i] + fpl[i] - eps, 2))

plt.plot(bpl, marker='^', label = '$MCBPL_t$')
plt.plot(fpl, marker='s', label = '$MCFPL_t$')
plt.plot(tpl, marker='o', label = '$MCDPL_t$')
plt.plot([eps for i in range(12)], marker='*', label = '$\epsilon_t$')
plt.title("不同时刻区间下的隐私泄露")
plt.xlabel("时刻区间")
plt.ylabel("隐私泄露")
plt.legend()
plt.show()
print(tpl)