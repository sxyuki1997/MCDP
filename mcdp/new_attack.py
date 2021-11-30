from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (6,5)

def plot_curve():
    x = [i*0.01 for i in range(100)]
    y = []
    for xx in x:
        y.append(0.84 * np.e**(-2.44*xx) + 0.13)

    ox=[0.36, 0.67, 0.19, 0.08, 0.07]

    oy=[0.5,0.3,0.65,0.9,0.8]

    # plt.scatter(x,y,marker='_',color='salmon', label="拟合曲线$\Phi(x_i)$")
    plt.scatter(ox,oy, marker='^', label="原始值$f(x_i)$")
    plt.xlabel('数据价值')
    plt.ylabel('攻击成功概率')
    # plt.title("拟合曲线")
    plt.legend()
    plt.savefig('sca.png')
    # plt.show()

# plot_curve()

def plot_geo(lamda, marker,line):
    # x = [i for i in range(-10, 11)]
    x = np.linspace(-10,10)

    y = []
    for i in range(len(x)):
        y.append((1 - lamda) / (1 + lamda) * lamda ** (abs(x[i])))

    plt.plot(x, y, marker=marker, linestyle = line, label="$\lambda$ = " + str(lamda))
    plt.fill_between(x, 0, y, where=abs(x)<=2,facecolor='grey', alpha=0.3)

    plt.xlabel("x")
    plt.ylabel("概率密度")
    # plt.title("Geo概率密度函数图")
    plt.title("容忍区间为$[-1,1]$的Geometric分布")

    plt.legend()
    # plt.show()

#
# plot_geo(0.3, 'x', '-')
# plot_geo(0.5, '*', '--')
# plot_geo(0.8, '.', '-.')

# plt.savefig('geo_3.png')


# plt.show()

def plot_geo_s(lamda, marker, line):
    # x = [i for i in range(-10, 11)]
    x = np.arange(-10,11,1)
    y = []
    for i in range(len(x)):
        y.append((1 - lamda) / (1 + lamda) * lamda ** (abs(x[i])))

    plt.plot(x, y, marker=marker, linestyle = line, label="$\lambda$ = " + str(lamda))
    plt.fill_between(x, 0, y, where=abs(x)<=1,facecolor='lightgrey')

    plt.xlabel("x")
    plt.ylabel("概率密度")
    # plt.title("Geo概率密度函数图")
    plt.title("容忍区间为$[-1,1]$的Geometric分布")

    plt.legend()
    # plt.show()

#
# plot_geo_s(0.3, 'x', '-')
# plot_geo_s(0.5, '*', '-')
# plot_geo_s(0.8, '.', '-')
#

# plt.savefig('geo_3.png')


# plt.show()

def plot_lamda():
    x = [i for i in range(-100, 100)]
    y = []
    for i in range(len(x)):
        if (x[i] != 0):
            y.append(np.e ** (-1 / x[i]))

    plt.plot(y)
    plt.xlabel("$\lambda$")
    plt.ylabel("y")
    plt.title("Lamda")
    plt.show()


# plot_lamda()


# plt.show()


def geo_mech(lamda):
    u1 = np.random.random()
    if u1 <= 0.5:
        add_noise = - (np.log(-(1 - lamda) / (1 + lamda) * np.log(lamda) * u1)) / np.log(lamda)
    else:
        add_noise = np.log((np.log(lamda) * (1 - lamda) * u1 - np.log(lamda) * (1 - lamda))) / np.log(lamda)
    # print(add_noise)
    return add_noise


# geo_mech(100)

def re_geo_mech(lamda):
    x = [i * 0.1 for i in range(-10, 10)]
    y = []
    for i in range(len(x)):
        if i == 0:
            y.append(0)
        elif i <= 0.5:
            y.append(- (np.log(-(1 - lamda) / (1 + lamda) * np.log(lamda) * x[i])) / np.log(lamda))
        else:
            y.append(np.log((np.log(lamda) * (1 - lamda) * x[i] - np.log(lamda) * (1 - lamda))) / np.log(lamda))

    plt.scatter(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Geo mechanism")
    plt.show()


# re_geo_mech(0.5)


def geo_hist(hist, lamda):
    n = len(hist)
    noised_hist = []
    acc = 0
    for i in range(n):
        noise = geo_mech(lamda)
        tmp = hist[i] + noise
        # print(noise)
        acc += 1 - abs(noise) / hist[i]
        noised_hist.append(tmp)
    # print(acc/12)
    return noised_hist


def main():
    hist = [40, 100, 160, 200, 560, 870, 960, 750, 400, 320, 220, 110]
    lamda = np.e ** 0.25

    noised_hist = geo_hist(hist, lamda)

    # plt.subplot(1,2,1)
    # plt.bar(height = hist, x=[i for i in range(1, 13)], width=1, color= "steelblue",edgecolor = "black")
    # plt.xlabel("t")
    # plt.ylabel("count of loc")
    # plt.title("original histogram for loc")

    # plt.subplot(1,2,2)
    # plt.bar(height = noised_hist, x=[i for i in range(1, 13)], width=1, color= "steelblue",edgecolor = "black")
    # plt.xlabel("t")
    # plt.ylabel("count of loc")
    # plt.title("noised histogram for loc")

    # plt.show()


def plot_eps_p():
    p = [i * 0.1 for i in range(6)]
    e = []
    for i in range(len(p)):
        e.append(np.e ** (-1 * p[i]))

    plt.plot(e)

    plt.show()

# plot_eps_p()


# main()

def plot_geo_distribution(lamda, marker):
    a = (lamda-1)/(lamda+1) / (np.log(lamda))
    x = [i for i in range(-10, 11)]
    y=[]
    for i in range(len(x)):
        if x[i] == 0:
            y.append(0.5)
        elif x[i]>0:
            y.append(1 - a*lamda**(x[i]))
        else:
            y.append(a*lamda**(-x[i]))
    plt.plot(x,y, marker=marker, label="$\lambda$="+str(lamda))
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.title("累计分布函数")
    plt.legend()
    plt.show()

# plot_geo_distribution(0.3, 'o')
# plot_geo_distribution(0.5, '^')
# plot_geo_distribution(0.8, 's')
# plt.savefig('geo_4.png')
#

def plot_eps_p():
    eps=[i*0.1 for i in range(1,100)]
    p = []
    for e in eps:
        lamda = np.e ** (-e)
        a = (lamda-1) / (lamda+1) / (np.log(lamda))
        p.append(1 - a*lamda)

    plt.plot(eps, p, linestyle= '--', label="N:1次", color='black')
    plt.xlabel("$\epsilon$")
    plt.ylabel("攻击成功概率")
    plt.title("一次查询下 $\epsilon$与攻击成功概率")

    plt.legend()
    # plt.show()
    # plt.savefig('attack_1.png')


# plot_eps_p()

def plot_attack(n):
    line = ['-', '--','-.',':']
    eps=[i*0.01 for i in range(1,500)]
    for k in range(n+1):
        accList = list()
        N=2*k+1
        for e in eps:
            acc=0
            lamda = np.e ** (-e)
            a = (lamda-1)/(lamda+1) / (np.log(lamda))
            for i in range(1, k+2):
                tmp = comb(N, k+i) * (1 - a*lamda) ** (k+i) * (a*lamda) ** (k+1-i)
                acc+=tmp
                acc=round(acc, 4)
            accList.append(acc)
#         print(accList)

        plt.plot(eps, accList, label="N:"+str(N)+'次', linestyle=line[k])
#         my_x_ticks = np.arange(0, 13, 1)
#         plt.xticks(my_x_ticks)
        plt.xlabel("$\epsilon$")
        plt.ylabel("攻击成功概率")
        plt.title("不同攻击次数下 $\epsilon$与攻击成功概率")
        plt.legend()
    # plt.savefig('attack_2.png')

    plt.show()

# plot_attack(3)

def plot_once_attack():
    eps=[i*0.1 for i in range(1,100)]
    p = []
    L = 1
    for e in eps:
        lamda = np.e ** (-e)
        a = (lamda - 1) / (lamda + 1) / np.log(lamda)
        L1 = 1 - a * lamda ** L
        L2 = a * lamda ** L
        p.append(L1-L2)

    plt.plot(eps, p, linestyle= '--', label="N:1次", color='black')
    plt.xlabel("隐私保护参数 $\epsilon$")
    plt.ylabel("攻击成功概率")
    plt.title("一次查询下 $\epsilon$与攻击成功概率")

    plt.legend()
    plt.show()
    # plt.savefig('attack_1.png')


# plot_once_attack()

def plot_attack_2(n):
    line = ['-', '--','-.',':']
    eps=[i*0.01 for i in range(1,500)]
    for k in range(n+1):
        accList = list()
        N=2*k+1
        for e in eps:
            acc=0
            lamda = np.e ** (-e)
            a = (lamda-1)/(lamda+1) / (np.log(lamda))
            for i in range(1, k+2):
                tmp = comb(N, k+i) * (1 - 2*a*lamda) ** (k+i) * (2*a*lamda) ** (k+1-i)
                acc+=tmp
                acc=round(acc, 4)
            accList.append(acc)
#         print(accList)

        plt.plot(eps, accList, label="N:"+str(N)+'次', linestyle=line[k])
#         my_x_ticks = np.arange(0, 13, 1)
#         plt.xticks(my_x_ticks)
        plt.xlabel("隐私保护参数 $\epsilon$")
        plt.ylabel("攻击成功概率")
        plt.title("不同攻击次数下 $\epsilon$与攻击成功概率")
        plt.legend()
    # plt.savefig('attack_2.png')

    plt.show()

# plot_attack_2(3)

def cal_once_attack(e):
    p = []
    L = 1
    lamda = np.e ** (-e)
    a = (lamda - 1) / (lamda + 1) / np.log(lamda)
    L1 = 1 - a * lamda ** L
    L2 = a * lamda ** L
    print(L1-L2)


cal_once_attack(3)