import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 8))

eps = 1

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

        BPL.append(round(L + e,2))

    return BPL


def plotMCBPL():
    p = [[[0.8,0.2],[0.1,0.9]], [[0.8, 0.2],[0,1]], [[0.8, 0.2],[1,0]], [[1,0],[0,1]]]
    seq = ['(1)','(2)','(3)','(4)']
    for i in range(len(p)):
        BPL_test = calBPL(p[i], eps , eps, 12)
        plt.subplot(2,2,i+1)
        FPL_test = []
        for j in range(len(BPL_test)-1, -1, -1):
            FPL_test.append(BPL_test[j])
        for i in range(12):
            MPL.append(BPL[i] + FPL[i] - ep)
        plt.plot(FPL_test, marker='.', label="$P_i^B$" + "=" + str(p[i]))
        plt.xlabel("时间")
        plt.ylabel("隐私泄露")
        plt.title(str(seq[i]) + " MCFPL随时间的变化趋势")

        plt.legend(loc=8)
        plt.tight_layout()

    plt.show()
    plt.savefig("mcfpl.png")


# plotMCBPL()

def calEps(eps):
    plt.figure(figsize=(6, 5))
    p = [[0.8,0.2],[0.1,0.9]]
    BPL_test = calBPL(p, eps , eps, 12)
    FPL_test = []
    for j in range(len(BPL_test)-1, -1, -1):
        FPL_test.append(BPL_test[j])
    MPL = []
    for i in range(12):
        MPL.append(round(BPL_test[i] + FPL_test[i] - eps,2))
    plt.plot(BPL_test, marker='^', label="MCBPL at t")
    plt.plot(FPL_test, marker='s', label="MCFPL at t")
    plt.plot(MPL, marker='o', label="MCDPL at t")
    plt.plot([eps for i in range(12)], marker='*', label="$\epsilon_t$")
    plt.xlabel("时间")
    plt.ylabel("隐私泄露")
    plt.title("不同时刻下不同类型的隐私泄露")
    plt.legend()
    plt.show()
    plt.savefig("mcdpl")

#
# eps = 0.19
# calEps(eps)
#

def calOriginEps():
    plt.figure(figsize=(6, 5))
    p = [[0.8,0.2],[0.1,0.9]]
    BPL_test = calBPL(p, eps , eps, 12)
    FPL_test = []
    for j in range(len(BPL_test)-1, -1, -1):
        FPL_test.append(BPL_test[j])
    MPL = []
    for i in range(12):
        MPL.append(round(BPL_test[i] + FPL_test[i] - eps,2))
    plt.plot(BPL_test, marker='^', label="MCBPL at t")
    plt.plot(FPL_test, marker='s', label="MCFPL at t")
    plt.plot(MPL, marker='o', label="MCDPL at t")
    plt.plot([eps for i in range(12)], marker='*', label="$\epsilon_t$")
    plt.xlabel("时间")
    plt.ylabel("隐私泄露")
    plt.title("不同时刻下不同类型的隐私泄露")
    plt.legend()
    plt.show()
    plt.savefig("mcdpl_origin.png")



calOriginEps()