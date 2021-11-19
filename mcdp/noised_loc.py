import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cal_price import utility

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (12,4)

titles = ['00-01', '02-03', '04-05', '06-07', '08-09', '10-11', '12-13',
          '14-15', '16-17', '18-19', '20-21', '22-23']

def geo_mech(lamda):
    u1 = np.random.random()
    if u1 <= 0.5:
        add_noise = - (np.log(-(1 - lamda) / (1 + lamda) * np.log(lamda) * u1)) / np.log(lamda)
    else:
        add_noise = np.log((np.log(lamda) * (1 - lamda) * u1 - np.log(lamda) * (1 - lamda))) / np.log(lamda)
    # print(add_noise)
    if add_noise <= 0:
        add_noise = -int(np.random.random()*1)

    return add_noise

# laplace加噪
def _lapalce_mech(e):
    beta = 1 / e
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 < 0.5:
        noise = int(beta * np.log(2 * u2))
    else:
        noise = int(-beta * np.log(2 - 2 * u2))
    if noise <= -3:
        noise = -3
    return noise

def geo_hist_generate(hist, lamda):
    noised_hist = []
    for i in hist:
        noised_hist.append(_lapalce_mech(lamda) + i)
    return noised_hist


def clean_origin():
    origin_time_locs=np.load("origin_time_locs.npy")
    for item in origin_time_locs:
        for i in range(65):
            if item[i] <= 20 and item[i] > 0:
                item[i] += int(np.random.random() * 8)
            elif item[i] == 0:
                item[i] += int(np.random.random() * 5)
        # print(item)

    for i in range(len(origin_time_locs)):
        hist = origin_time_locs[i]
        plt.subplot(2, 6, i + 1)
        plt.bar(height=hist, x=[k for k in range(1, 66)], width=1, color='SteelBlue', edgecolor="black")
        plt.title("$t=$" + str(i))
        plt.tight_layout()
    # np.save("origin_time_locs_mod.npy", origin_time_locs)
    plt.show()
    return origin_time_locs

# clean_origin()
# origin_time_locs=np.load("origin_time_locs_mod.npy")

def plot_origin(origin_time_locs):
    plt.rcParams['figure.figsize'] = (15, 8)
    WD  = []
    for k in range(65):
        tmp = []
        for i in range(len(origin_time_locs)):
            tmp.append(origin_time_locs[i][k])
        plt.subplot(6,11,k+1)
        x = [i for i in range(12)]
        plt.bar(x=x, height=tmp, color='SteelBlue', edgecolor = "black")
        plt.title("$loc$" + str(k+1))
        plt.tight_layout()

        # # 计算两个直方图之间的距离
        # res_utility = utility.Utility(tmp, origin_time_locs[])
        # W = res_utility._cal_wasserstein()
        # WD.append(W)

    plt.show()
    # return origin_time_locs

# plot_origin(origin_time_locs)



def main():
    # clean_origin()
    # plot_origin()
    # origin_time_locs=np.load("origin_time_locs_mod.npy")
    # plot_origin()
    origin_time_locs = clean_origin()
    WD = []
    ACC = []
    MSE = []

    plt.rcParams['figure.figsize'] = (12, 4)
    Lamda = [0.35, 0.34, 0.35, 0.37, 0.37, 0.36, 0.36, 0.38, 0.36, 0.33, 0.35, 0.32]
    noised_time_locs = []

    for j in range(len(origin_time_locs)):
        lamda = Lamda[j]
        eps = round(-np.log(lamda),2)

        hist = origin_time_locs[j]
        noised_hist = geo_hist_generate(hist, eps)
        noised_time_locs.append(noised_hist)

        plt.subplot(2,6,j+1)
        plt.bar(height=noised_hist, x = [k for k in range(1, 66)], width = 1, color='SteelBlue', edgecolor = "black")
        plt.tight_layout()
        plt.title("$t=$" + str(j) + ", $\epsilon=$" + str(eps) )

        # 计算两个直方图之间的距离
        res_utility = utility.Utility(hist, noised_hist)
        W = res_utility._cal_wasserstein()
        WD.append(W)

        # 计算直方图统计的精度
        final_acc = []
        mse = 0
        for i in range(len(hist)):
            if hist[i] == 0:
                continue
            acc = 1 - (abs(noised_hist[i] - hist[i]) / hist[i])
            final_acc.append(acc)
            mse += (noised_hist[i] - hist[i]) ** 2

        ACC.append(np.mean(final_acc))
        MSE.append(mse / len(hist))


    plt.show()

    print("直方图距离：", WD)
    print("精度：", ACC)
    print("MSE：", MSE)


    plt.rcParams['figure.figsize'] = (15, 4)

    plt.subplot(1,3,1)
    plt.plot(WD, label="wasserstein distance", marker="s")
    mean_wd = np.mean(WD)
    plt.plot([mean_wd for k in range(12)], marker='_', linestyle= 'dotted',label="均值")
    plt.xlabel("时刻区间")
    plt.ylabel("W距离（wasserstein distance）")
    plt.title("(1) 加噪前后直方图分布的距离")
    plt.legend()

    plt.tight_layout()

    plt.subplot(1,3,2)
    plt.plot(ACC, label="精度", marker="^")
    mean_acc = np.mean(ACC)
    plt.plot([mean_acc for k in range(12)], marker='_', linestyle= 'dotted',label="均值")
    plt.xlabel("时刻区间")
    plt.ylabel("精度")
    plt.title("(2) 直方图的平均精度")
    plt.legend()

    plt.tight_layout()

    plt.subplot(1,3,3)
    plt.plot(MSE, label="MSE", marker='*')
    mean_mse = np.mean(MSE)
    plt.plot([mean_mse for k in range(12)], marker='_', linestyle= 'dotted', label="均值")
    plt.xlabel("时刻区间")
    plt.ylabel("MSE")
    plt.title("(3) 直方图发布的MSE")
    plt.tight_layout()
    plt.legend()
    plt.show()

    plot_origin(origin_time_locs)
    plot_origin(noised_time_locs)

main()
