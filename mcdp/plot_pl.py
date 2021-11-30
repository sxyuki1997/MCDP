import numpy as np
import matplotlib.pyplot as plt
import time

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 4))

beta = 2.5
bpl=[2.5, 2.906, 2.94, 2.94, 2.94, 2.94, 2.94, 2.94, 2.94, 2.94, 2.94, 2.94]
fpl=[2.557, 2.557, 2.557, 2.557, 2.557, 2.557, 2.557, 2.557, 2.557, 2.557, 2.557, 2.5]
udpl=[beta for i in range(12)]
# mcdpl=[5.12,6.58,	6.61,	6.61,	6.61,	6.61,	6.61,	6.61,	6.61,	6.61,	6.56,	4.74]
eps = [0.7985076962177716, 0.8209805520698302, 0.7765287894989963, 0.7339691750802004, 0.7133498878774648, 0.7550225842780328, 0.7550225842780328, 0.7133498878774648, 0.7550225842780328, 0.843970070294529, 0.7765287894989963, 0.8675005677047231]
mcdpl = []

lalist = [0.26, 0.19, 0.3, 0.41, 0.43, 0.37, 0.35, 0.44, 0.33, 0.17, 0.28, 0.08]
for i in range(len(bpl)):
    mcdpl.append(bpl[i] + fpl[i] - beta)

plt.subplot(1,2,1)
plt.plot(bpl, marker='^', label = '$MCBPL_t$')
plt.plot(fpl, marker='s', label = '$MCFPL_t$')
plt.plot(udpl, marker='*', label = '$UDPL_t$')
plt.plot(mcdpl, marker='o', label = '$MCDPL_t$')
# plt.plot(eps, marker='X', label = '$\epsilon_t$')


plt.title("(1) 不同时间段下不同类型的隐私泄露")
plt.xlabel("时间段 ($t$)")
plt.ylabel("隐私泄露")
plt.legend(loc=7)

plt.tight_layout()

plt.subplot(1,2,2)
plt.plot(eps, marker='X', label = '$\epsilon_t$', color="slateblue")
plt.xlabel("时间段 ($t$)")
plt.ylabel("隐私保护参数 $\epsilon$")
plt.title("(2) 不同时间段下分配的隐私保护参数")
plt.legend()

plt.tight_layout()

plt.show()