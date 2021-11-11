import numpy as np
import matplotlib.pyplot as plt
import time

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 8))

eps = 1

def progress(percent, width=50):
    '''
    进度打印功能
    每次的输入是已经完成总任务的百分之多少

    '''
    if percent >= 100:
        percent = 100

    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    print('\r%s %d%%' % (show_str, percent), end='')


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
        progress(100 * t/(T-1))

    return BPL

# 转移矩阵设置

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

Pt = generateLoc(30, 1)[0]
# print(Pt)
P = Pt
# P = [[0.06, 0.85, 0.09], [0.3, 0.38, 0.32], [0.17, 0.46, 0.37]]
T = 12
startT = time.time()
bpl = calBPL(P, eps , eps, T)
endT = time.time()
interval = endT - startT
print("=====运行时间=======：", interval * 1000)
print("BPL:", bpl)


def plotMCBPL():
    p = [[[0.8,0.2],[0.1,0.9]], [[0.8, 0.2],[0,1]], [[0.8, 0.2],[1,0]], [[1,0],[0,1]]]
    seq = ['(1)','(2)','(3)','(4)']
    for i in range(len(p)):
        BPL_test = calBPL(p[i], eps , eps, 12)
        plt.subplot(2,2,i+1)
        FPL_test = []
        for j in range(len(BPL_test)-1, -1, -1):
            FPL_test.append(BPL_test[j])
        plt.plot(FPL_test, marker='.', label="$P_i^B$" + "=" + str(p[i]))
        plt.xlabel("时间")
        plt.ylabel("隐私泄露")
        plt.title(str(seq[i]) + " MCFPL随时间的变化趋势")

        plt.legend(loc=8)
        plt.tight_layout()

    plt.show()
    plt.savefig("../img/mcfpl.png")


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
    print("BPL:",BPL_test)
    print("FPL:",FPL_test)
    print("MCDPL:", MPL)
    plt.savefig("../img/mcdpl.png")


# eps = 0.19
# calEps(eps)


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
    plt.savefig("../img/mcdpl_origin.png")



# calOriginEps()

