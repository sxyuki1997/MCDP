from numpy.random import random
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 8))

ep = 0.36

def progress(percent, width=50):
    '''进度打印功能
       每次的输入是已经完成总任务的百分之多少

    '''
    if percent >= 100:
        percent = 100

    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    print('\r%s %d%%' % (show_str, percent), end='')

# calP(12, 0.8)


'''
输入n:
输出：生成n*n的位置关联矩阵
'''
def generateLoc(n, T):
    res = list()
    for t in range(T):
        m = list()
        for i in range(n):
            b = np.random.dirichlet(np.ones(n), size=1)
            b = np.around(b, 2).tolist()[0]
            while 0.00 in b:
                b = np.random.dirichlet(np.ones(n), size=1)
                b = np.around(b, 2).tolist()[0]

            m.append(b)

        res.append(m)

    return res

# print(generateLoc(10, 10))


'''
多项式时间内计算
BPL
'''


def calBPL(Pt, a, e, T):
    BPL = [a]
    for t in range(1,T):
        a = BPL[t-1]

        L=0
        # 任取转移矩阵P中不相等的两行p,q
        k=len(Pt)
        p = []
        q = []
        for ii in range(k):
            for jj in range(ii, k):
                if ii == jj:
                    continue

                P=Pt[ii]
                Q=Pt[jj]

                n = len(P)

                for j in range(n):
                    if P[j]>Q[j]:
                        p.append(P[j])
                        q.append(Q[j])

                up=False

                while True:
                    sum_p = sum(p)
                    sum_q = sum(q)
                    nn=len(p)

                    for i in range(nn-1,-1,-1):
                        if q[i]!=0 and p[i]/q[i] <= (sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1):
                            p.remove(p[i])
                            q.remove(q[i])

                            up=True

                    if up==False:

                        break

                if L<np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1)):
                    L = np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1))

        BPL.append(L + e)

    return BPL



a = [0.1, 0.04, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
b =  [1.83, 1.11, 0.85, 0.71, 0.62, 0.56, 0.51, 0.47, 0.44, 0.42, 0.4, 0.38]

Pt = generateLoc(2, 3)
BPL = calBPL([[0.8,0.2],[0.1,0.9]], ep , ep, 12)
p = [[[0.8,0.2],[0.1,0.9]], [[0.8, 0.2],[0,1]], [[0.8, 0.2],[1,0]], [[1,0],[0,1]]]
seq = ['(1)','(2)','(3)','(4)']
for i in range(len(p)):
    BPL_test = calBPL(p[i], 1.83 , 1.83, 12)
    plt.subplot(2,2,i+1)
    FPL_test = []
    for j in range(len(BPL_test)-1, -1, -1):
        FPL_test.append(BPL_test[j])
    plt.plot(BPL_test, marker='.', label="$P_i^B$" + "=" + str(p[i]))
    plt.xlabel("时间")
    plt.ylabel("隐私泄露")
    plt.title(str(seq[i]) + " MCBPL随时间的变化趋势")

    plt.legend(loc=8)
    plt.tight_layout()

plt.show()


print(BPL_test)
time = [i for i in range(12)]
BPLE = []
for i in range(12):
    BPLE.append(BPL[i]-1.83)


# print(BPLE)
plt.plot(BPL_test, marker = '^', label= "MCBPL at t")
plt.xlabel("时间")
plt.ylabel("隐私泄露")
plt.title("不同时刻下的MCBPL")
plt.legend()
# plt.show()

# plt.plot(BPLE, marker = '.', label= "EPL at t")
# plt.xlabel("t")
# plt.ylabel("leakage")
# plt.title("event-level leakage within time under temporal correlations")
# plt.legend()
#
# plt.show()



list = []
for i in range(len(a)):
    tmp = (b[i]-2*a[i])
    list.append(tmp)
print(list)

# plt.plot(list)
# plt.xlabel("t")
# plt.ylabel("epsilon")
# plt.title("total privacy budget within time")
# plt.show()


'''
生成位置直方图数据
'''
# def generateLocHist(n,a,b):
#     res = []
#     for i in range(n):
#         tmp = np.random.randint(a, b)
#         res.append(tmp)
#     return res
#

# res = generateLocHist(12, 10, 100)
res = [40, 100,  160,  200, 560, 870, 960, 750, 400, 320, 220, 110]
# print(res)
#
# plt.subplot(1,2,1)
# plt.bar(height = res, x=[i for i in range(1, 13)], width=1, color= "steelblue",edgecolor = "black")
# plt.xlabel("t")
# plt.ylabel("count of loc")
# plt.title("original histogram for loc")

'''
laplace加噪
'''
def _laplace_mech(e):
    beta = 20 / e
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 <= 0.5:
        add_noise = beta * np.log(2 * u2)
    else:
        add_noise = -beta * np.log(2 - 2 * u2)
    return add_noise


'''
计算加噪后的直方图
'''
def noised_hist(hist, e):
    n=len(hist)
    noised_hist = []
    acc = 0
    for i in range(n):
        noise=_laplace_mech(e[i])
        tmp = hist[i] + noise
        print(noise)
        acc += 1- abs(noise) / hist[i]
        noised_hist.append(tmp)
    print(acc/12)
    return noised_hist



# noised_hist = noised_hist(res, list)
# plt.subplot(1,2,2)
# plt.bar(height = noised_hist, x=[i for i in range(1, 13)], width=1, color= "steelblue",edgecolor = "black")
# plt.xlabel("t")
# plt.ylabel("count of loc")
# plt.title("noised histogram for loc")
#
#
#
#
# plt.show()
#




BPL = [1.83, 3.0552393333332164, 3.5676786660915525, 3.690140348993917, 3.7129548944726025, 3.7169622715016892, 3.7176585261731425, 3.71777926422177, 3.7178001945323196, 3.7178038226564123, 3.7178044515602564, 3.7178045605750945]
target = []
for i in range(12):
    target.append(round(BPL[i]*2-1.83-1.83,2))
print(target)
# plt.plot(target, marker = '.')
# plt.xlabel("t")
# plt.ylabel("$\epsilon_t$")
# plt.title("event-level privacy budget within time")
# plt.show()

plt.plot(BPL, marker = '^', label= "MCBPL at t")
plt.xlabel("时间")
plt.ylabel("隐私泄露")
plt.title("不同时刻下的MCBPL")
plt.legend()
# plt.show()
'''
计算FPL
'''
def calFPL(Pt, a, e, T):
    BPL = [a]
    for t in range(1,T):
        a = BPL[t-1]

        L=0
        # 任取转移矩阵P中不相等的两行p,q
        k=len(Pt)
        p = []
        q = []
        for ii in range(k):
            for jj in range(ii, k):
                if ii == jj:
                    continue

                P=Pt[ii]
                Q=Pt[jj]

                n = len(P)

                for j in range(n):
                    if P[j]>Q[j]:
                        p.append(P[j])
                        q.append(Q[j])

                up=False

                while True:
                    sum_p = sum(p)
                    sum_q = sum(q)
                    nn=len(p)

                    for i in range(nn-1,-1,-1):
                        if q[i]!=0 and p[i]/q[i] <= (sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1):
                            p.remove(p[i])
                            q.remove(q[i])

                            up=True

                    if up==False:

                        break

                if L<np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1)):
                    L = np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1))

        BPL.append(L + e)

    return BPL




BPL = calFPL([[0.8,0.2],[0.1,0.9]], ep,  ep, 12)
print(BPL)
FPL=[]
for i in range(11, -1, -1):
    FPL.append(BPL[i])


plt.plot(FPL, marker = 's', label= "MCFPL at t")
plt.xlabel("t")
plt.ylabel("leakage")
plt.title("MFPL within time under temporal correlations")
plt.legend()
# plt.show()

MPL = []
for i in range(12):
    MPL.append(BPL[i] + FPL[i]-ep)
print("-------PL-------")
print(BPL)
print(FPL)
print(MPL)

plt.plot(MPL, marker = 'o', label= "MCDPL at t")
plt.xlabel("t")
plt.ylabel("leakage")
plt.title("privacy leakage within time under temporal correlations")
plt.legend()


plt.plot([ep for i in range(12)], marker = '*', label="$\epsilon_t$")
plt.xlabel("时间")
plt.ylabel("隐私泄露")
plt.title("不同时刻下各种类型的隐私泄露")
plt.legend()



# plt.show()


def calMPL(Pt, a, e, T):
    BPL = [a]
    for t in range(1,T):
        a = BPL[t-1]

        L=0
        # 任取转移矩阵P中不相等的两行p,q
        k=len(Pt)
        p = []
        q = []
        for ii in range(k):
            for jj in range(ii, k):
                if ii == jj:
                    continue

                P=Pt[ii]
                Q=Pt[jj]

                n = len(P)

                for j in range(n):
                    if P[j]>Q[j]:
                        p.append(P[j])
                        q.append(Q[j])

                up=False

                while True:
                    sum_p = sum(p)
                    sum_q = sum(q)
                    nn=len(p)

                    for i in range(nn-1,-1,-1):
                        if q[i]!=0 and p[i]/q[i] <= (sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1):
                            p.remove(p[i])
                            q.remove(q[i])

                            up=True

                    if up==False:

                        break

                if L<np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1)):
                    L = np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1))

        BPL.append(L + e)

    return BPL



BPL = calMPL([[0.8,0.2],[0.1,0.9]], ep,  ep, 12)
print(BPL[-1])
