import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from cal_price import utility
from cal_price.calProb import CalProbability

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 600
plt.rcParams['figure.figsize'] = (10,6)

# charge_data = pd.read_csv("../data/insurance.csv")
heart_data = pd.read_csv("../data/heart.csv")
heart_data_url = "../data/heart.csv"
credit_data = pd.read_csv("../data/german_credit_data.csv")
income_data_url = "../data/adult_2.csv"
age = heart_data["age"]
# age = credit_data["Age"]
N = len(age)

# 设定目标直方图的组数、桶范围
# n_equal_bins = [i for i in range(10, 90)]
n_equal_bins = [10, 15, 20]
opt_epsilon = []
WD = []
MSE = []

# 计算目标直方图的数据价值
# 计算相应的攻击成功概率
prob = CalProbability(income_data_url)._cal_prob()
print(prob)


def geo_mech(lamda):
    u1 = np.random.random()
    if u1 <= 0.5:
        add_noise = - (np.log(-(1 - lamda) / (1 + lamda) * np.log(lamda) * u1)) / np.log(lamda)
    else:
        add_noise = np.log((np.log(lamda) * (1 - lamda) * u1 - np.log(lamda) * (1 - lamda))) / np.log(lamda)
    # print(add_noise)
    return add_noise

def geo_hist_generate(hist, lamda):
    noised_hist = []
    for i in hist:
        noised_hist.append(geo_mech(lamda) + i)
    return noised_hist


for k in range(len(n_equal_bins)):
    # original histogram
    plt.subplot(2, 3, k+1)
    plt.hist(x = age, bins =n_equal_bins[k], color='SteelBlue', edgecolor = "black")
    plt.xlabel("age")
    plt.ylabel("count")
    plt.title("原始直方图" + " ($N$="+ str(n_equal_bins[k]) +")")
    plt.tight_layout()

    # DP Histogram 1
    hist, bin_edges= np.histogram(age, bins=n_equal_bins[k])

    # adding lap noise
    hist = hist.tolist()
    print("original hist:", hist)
    x = hist
    # 设置lamda
    lamda = 0.43
    x_noised = geo_hist_generate(x, lamda)

    # opt_eps = res._laplace_mech()[1]
    # opt_epsilon.append(opt_eps)
    # opt_eps = 0.21
    print("noised hist:", x_noised)

    final_acc = []
    mse = 0
    for i in range(len(x)):
        acc = 1 - (abs(x_noised[i] - x[i]) / x[i])
        final_acc.append(acc)
        mse += (x_noised[i] - x[i]) ** 2

    print("final_acc:", final_acc)
    print("mean_acc:", np.mean(final_acc))
    print("mse:", mse / len(x))
    MSE.append(mse / len(x))

    # plt.hist(hist.tolist(),bins=bin_edges,histtype='bar',rwidth=10,edgecolor="black")

    # ind = np.arange(20, 90, int((90-17)/n_equal_bins))  # the x locations for the groups
    # ind = [20, 40, 60, 80]
    ind = np.arange(len(hist))
    print(ind)
    width = 1 # the width of the bars

    plt.subplot(2, 3, k+4)
    plt.bar(ind , x_noised, width, color='SteelBlue', edgecolor='black')
    plt.xlabel("age")
    plt.ylabel("count")
    plt.title("差分隐私直方图 ($\epsilon$="+ str(round(-np.log(lamda), 2)) + ")")
    plt.tight_layout()

    # 计算两个直方图之间的距离
    res_utility = utility.Utility(hist, x_noised)
    F = res_utility._cal_f_divergence()
    H = res_utility._cal_hellinger()
    B = res_utility._cal_bhattacharyya()
    W = res_utility._cal_wasserstein()
    WD.append(W)
    print("===========UTILITY===============")
    print("F=", F)
    print("H=", H)
    print("B=", B)
    print("W=", W)

    print("lamda=", lamda)

# plt.show()

# 收敛函数
# plt.plot(n_equal_bins, opt_epsilon)
# plt.xlabel("bins")
# plt.ylabel("epsilon")
# plt.title("Epsilon under different bins")

plt.savefig('../img/heart_hist.png')
plt.show()
print("W距离：", WD)
print("MSE:", MSE)
