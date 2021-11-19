import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (10,4)


# corr_all = np.load("corr_all.npy")
loc_num = [24, 33, 58, 40, 38, 47, 60, 34, 15, 22, 9, 15]
user_num = [14, 18, 33, 23, 23, 34, 41, 19, 8, 9, 6, 11]

degree = [5, 5, 14, 13, 13, 14, 17, 12, 4, 3, 2, 1]

LA = []
lalist = []
eps = 3.25
Lamda = []
for i in range(len(user_num)):
    m = 20
    la = round(m*degree[i] / (loc_num[i]*16) , 2)
    print(la)
    lalist.append(round(la,2))
    lamda = round((1 + la/2) / eps, 2)
    e = -np.log(lamda)
    LA.append(e)
    print(lamda, e)
    Lamda.append(lamda)

print(LA)
print(degree)
print(Lamda)
print(lalist)

plt.subplot(1,2,1)

degree = [5, 5, 14, 13, 13, 14, 17, 12, 4, 3, 2, 1]
lalist = [0.26, 0.19, 0.3, 0.41, 0.43, 0.37, 0.35, 0.44, 0.33, 0.17, 0.28, 0.08]
plt.scatter(degree, lalist, marker='o', label="$l_A$")
plt.title("(1) 用户关联程度与关联泄露系数")
plt.xlabel("用户关联程度（max_degree）")
plt.ylabel("关联泄露系数（$l_A$）")
plt.legend()
plt.tight_layout()


plt.subplot(1,2,2)
plt.plot(lalist, marker='o', label="$l_A^t$")
# plt.title("度与关联泄露系数")
plt.xlabel("用户关联程度（max_degree）")
plt.ylabel("用户关联程度与关联泄露系数（$l_A$）")
plt.legend()
# plt.show()

t = [i for i in range(12)]
plt.plot(t, LA, marker='p', label="$\epsilon_t$")
plt.title("(2) 用户关联和隐私保护参数")
plt.xlabel("时刻区间")
plt.ylabel("参数值")
plt.legend()
plt.tight_layout()

plt.show()