import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (12,4)


corr_all = np.load("corr_all.npy")
degree = []
loc_num = [24, 33, 58, 40, 38, 47, 60, 34, 15, 22, 9, 15]
user_num = [14, 18, 33, 23, 23, 34, 41, 19, 8, 9, 6, 11]

degree_sum = {}
mean_degree = []
# 计算每个时刻区间最大的度，一个用户至多和几个用户关联
for item in corr_all:
    tmp = []
    dmap = {}
    maxd = 0
    for ele in item:
        uid = ele[0]
        if uid in dmap:
            dmap[uid] += 1
        else:
            dmap[uid] = 1
    for key in dmap:
        if dmap[key] >= maxd:
            maxd=dmap[key]
        tmp.append(dmap[key])
    degree.append(maxd)
    mean_degree.append(np.mean(tmp))

LA = []
lalist = []
eps = 4.7
for i in range(len(user_num)):
    m = 20
    la = round(m*degree[i] / (loc_num[i]*16) , 2)
    print(la)
    lalist.append(la)
    lamda = round((1 + la/2) / eps, 2)
    e = -np.log(lamda)
    LA.append(e)
    print(lamda, e)

print(LA)
print(degree)

plt.rcParams['figure.figsize'] = (6,5)
plt.scatter(degree, lalist, marker='o', label="$l_A$")
plt.title("度与关联泄露系数")
plt.xlabel("用户关联程度（max_degree）")
plt.ylabel("用户关联程度与关联泄露系数（$l_A$）")
plt.legend()
plt.show()