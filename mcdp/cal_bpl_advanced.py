import numpy as np
import matplotlib.pyplot as plt
import time

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 8))

eps = 6.66

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
            for jj in range(k):
                if ii != jj:
                    P=Pt[ii]
                    Q=Pt[jj]

                    n = len(P)

                    for j in range(n):
                        if P[j]>Q[j]:
                            p.append(P[j])
                            q.append(Q[j])

                    up=False

                    while True:
                        print("========executing-------" + str(t))
                        sum_p = sum(p)
                        sum_q = sum(q)
                        nn=len(p)
                        origin_p = p
                        origin_q = q

                        for i in range(nn-1,-1,-1):
                            if q[i]!=0 and p[i]/q[i] <= (sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1):
                                p.remove(p[i])
                                q.remove(q[i])
                                up=True

                        if up==False or (p == origin_p and q == origin_q):
                            break

                    if L<np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1)):
                        L = np.log((sum_p*((np.e**(a))-1)+1) / (sum_q*((np.e**(a))-1)+1))

        BPL.append(round(L + e,2))
        print("========运行中" + str(t))
        # progress(100 * t/(T-1))

    return BPL

# 转移矩阵设置

'''
输入n:
输出：生成n*n的位置关联矩阵
'''
def generateLoc(n, T, s):
    res = list()
    for t in range(T):
        m = list()
        for i in range(n):
            b = np.random.normal(loc=5, scale=s, size=65)
            b = np.round(b, 3).tolist()
            for k in range(len(b)):
                b[k] = np.round(b[k]/np.sum(b), 3)
            # while 0.00 in b:
            #     b = np.random.dirichlet(np.ones(n), size=1)
            #     b = np.around(b, 3).tolist()[0]

            m.append(b)

        res.append(m)
        print(m)

    return res
BPL = []
FPL = []
TPL = []
# 65个位置之间的关联
# P = [[1/65 for i in range(65)] for k in range(65)]
s = 1.45
PB = generateLoc(65,1,s)[0]
PF = generateLoc(65,1,s)[0]
# print(PB)
T = 12
startT = time.time()
bpl = calBPL(PB, eps , eps, T)
fpl = calBPL(PF, eps, eps, T)
fpl.reverse()
tpl = []
for i in range(len(bpl)):
    tpl.append(bpl[i] + fpl[i] - eps)
print("bpl", bpl)
print("fpl", fpl)
print("TPL:", tpl)
print("maxpl:", max(tpl))

endT = time.time()
interval = endT - startT
print("=====运行时间(s)=======：", interval)