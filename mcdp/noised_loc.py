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
        add_noise = 0
    return add_noise

def geo_hist_generate(hist, lamda):
    noised_hist = []
    for i in hist:
        noised_hist.append(geo_mech(lamda) + i)
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
        plt.title(titles[i] + "时刻区间")
        plt.tight_layout()
    np.save("origin_time_locs_mod.npy", origin_time_locs)

    plt.show()

# clean_origin()
origin_time_locs=np.load("origin_time_locs_mod.npy")

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
        plt.title("位置簇" + str(k+1))
        plt.tight_layout()

        # # 计算两个直方图之间的距离
        # res_utility = utility.Utility(tmp, origin_time_locs[])
        # W = res_utility._cal_wasserstein()
        # WD.append(W)

    plt.show()
    # return origin_time_locs

plot_origin(origin_time_locs)



def main():
    # clean_origin()
    # plot_origin()
    origin_time_locs=np.load("origin_time_locs_mod.npy")
    # plot_origin()
    WD = []
    ACC = []
    MSE = []
    lamda = 0.3
    plt.rcParams['figure.figsize'] = (12, 4)
    noised_time_locs = []

    for j in range(len(origin_time_locs)):
        hist = origin_time_locs[j]
        noised_hist = geo_hist_generate(hist, lamda)
        noised_time_locs.append(noised_hist)
        plt.subplot(2,6,j+1)
        plt.bar(height=noised_hist, x = [k for k in range(1, 66)], width = 1, color='SteelBlue', edgecolor = "black")
        plt.tight_layout()
        # plt.legend()
        plt.title(titles[j] + "时刻区间")

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

    plot_origin(noised_time_locs)

# main()