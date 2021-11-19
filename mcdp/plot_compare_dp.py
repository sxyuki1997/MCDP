import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(12, 5))

target = [6.66 for i in range(12)]
mean_real_pl = [9.77, 27.43, 6.61]
mean_extra_pl = [3.11, 21.24, -0.05]
TPL = [8.23, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 9.720000000000002, 8.15]
BDPL=[]
lalist = [0.26, 0.19, 0.3, 0.41, 0.43, 0.37, 0.35, 0.44, 0.33, 0.17, 0.28, 0.08]
MCDPL = [5.12,	6.58,	6.61,	6.61,	6.61,	6.61,	6.61,	6.61,	6.61,	6.61,	6.56,	4.74]
for i in range(len(lalist)):
    BDPL.append(1/np.e**(-3.25) * (1+lalist[i] / 2))

plt.subplot(1,2,1)
plt.plot(BDPL, marker ='^', label="$TCDPL_t$")
plt.plot(TPL, marker='s', label="$BDPL_t$")
plt.plot(MCDPL, marker='o', label='$MCDPL_t$')
plt.plot(target, marker='*', label="$\epsilon_t$")

# plt.plot(Extra, marker ='s', label="平均额外隐私泄露")

plt.legend()
plt.title('不同时刻区间的隐私泄露对比')
# plt.xticks([0,1,2], ['BDP', 'TCDP', 'MCDP'])
plt.xlabel("时刻区间")
plt.ylabel("隐私泄露")


plt.subplot(1,2,2)

extra_tpl = []
extra_bpl=[]
extra_mcbpl = []
for i in range(len(TPL)):
    extra_tpl.append(BDPL[i]-6.66)
    extra_bpl.append(TPL[i]-6.66)
    extra_mcbpl.append(MCDPL[i]-6.66)
print("tpl", np.mean(TPL))
print("bpl:",np.mean(BDPL))
print("extra_tpl", np.mean(extra_tpl))
print("extra_bpl", np.mean(extra_bpl))

plt.plot(extra_tpl, marker ='^', label="extra_$TCDPL_t$")
plt.plot(extra_bpl, marker='s', label="extra_$BDPL_t$")
plt.plot(extra_mcbpl, marker='o', label='extra_$MCDPL_t$')
plt.plot([0 for i in range(12)], linestyle='dotted')
plt.legend()
plt.title('不同时刻区间的额外隐私泄露对比')
# plt.xticks([0,1,2], ['BDP', 'TCDP', 'MCDP'])
plt.xlabel("时刻区间")
plt.ylabel("额外隐私泄露")

plt.show()