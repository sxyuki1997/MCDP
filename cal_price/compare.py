import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 600
plt.rcParams['figure.figsize'] = (10,8)


# Heart Dataset
lapalce_acc = [0.71, 0.69, 0.52]
geo_acc = [0.80,0.83,0.80]

laplace_w = [1.5, 1.53, 1.85]
geo_w = [1.32, 1.08, 1.26]

laplace_mse= [3.1, 3.53, 3.95]
geo_mse = [2.11,2.91,2.42]

# Income Dataset
# lapalce_acc = [0.97, 0.92, 0.92]
# geo_acc = [0.97,0.93,0.91]
#
# laplace_w = [1.9, 2.0, 1.95]
# geo_w = [1.28, 1.74, 1.43]
#
# laplace_mse= [3.7, 4.0, 3.85]
# geo_mse = [1.75,6.42,3.28]

def _plot_compare():
    x = np.arange(3)
    bar_width = 0.35

    tick_label = ["10", "15", "20"]

    plt.subplot(1,4,1)


    plt.bar(x, lapalce_acc, bar_width, align="center", color="seashell", label="Lap机制", alpha=0.5, edgecolor='black')
    plt.bar(x+bar_width, geo_acc, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

    plt.xticks(x+bar_width/2, tick_label)

    plt.legend(loc = 4)

    plt.xlabel("直方图桶数")
    plt.ylabel("平均精度")
    plt.title("数据平均精度对比")
    plt.subplots_adjust(wspace=0.3)
    plt.tight_layout()

    plt.subplot(1,3,2)

    plt.bar(x, laplace_mse, bar_width, align="center", color="seashell", label="Lap机制", alpha=0.5, edgecolor='black')
    plt.bar(x+bar_width, geo_mse, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

    plt.xticks(x+bar_width/2, tick_label)

    plt.legend(loc = 4)

    plt.xlabel("直方图桶数")
    plt.ylabel("MSE")
    plt.title("数据MSE对比")
    plt.subplots_adjust(wspace=0.3)
    plt.tight_layout()

    plt.subplot(1,3,3)

    plt.bar(x, laplace_w, bar_width, align="center", color="seashell", label="Lap机制", alpha=0.5, edgecolor='black')
    plt.bar(x+bar_width, geo_w, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

    plt.xticks(x+bar_width/2, tick_label)

    plt.legend(loc = 4)

    plt.xlabel("直方图桶数")
    plt.ylabel("w距离")
    plt.title("直方图加噪前后分布差异对比")
    plt.tight_layout()


    plt.savefig("../img/compared_heart_acc.png")
    plt.show()

def _plot_time():
    # plt.rcParams['figure.figsize'] = (10, 8)

    t11 = [244, 1220, 2741]
    t12 = [7, 17, 34]
    t21 = [5,6,7]
    t22 = [4,4,4]


    x = np.arange(3)
    bar_width = 0.35

    tick_label = ["单次查询", "多次查询", "组合查询"]

    plt.subplot(2, 2, 1)

    plt.bar(x, t11, bar_width, align="center", color="seashell", label="Adult", alpha=0.5, edgecolor='black')
    # plt.bar(x+bar_width, t12, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

    plt.xticks(x, tick_label)

    plt.legend(loc = 4)

    plt.xlabel("($a$)")
    plt.ylabel("运行时间($ms$)")
    plt.title("计算$\epsilon$的运行时间(优化前)")
    plt.subplots_adjust(wspace=0.3)
    plt.tight_layout()

    plt.subplot(2,2,2)

    plt.bar(x, t12, bar_width, align="center", color="dimgrey", label="Heart", alpha=0.5, edgecolor='black')
    # plt.bar(x+bar_width, t12, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

    plt.xticks(x, tick_label)

    plt.legend(loc = 4)

    plt.xlabel("($b$)")
    plt.ylabel("运行时间($ms$)")
    plt.title("计算$\epsilon$的运行时间(优化前)")
    plt.subplots_adjust(wspace=0.3)
    plt.tight_layout()


    plt.subplot(2,2,3)


    plt.bar(x, t21, bar_width, align="center", color="seashell", label="Adult", alpha=0.5, edgecolor='black')
    plt.bar(x+bar_width, t22, bar_width,  align="center",color="dimgrey", label="Heart", alpha=0.5, edgecolor='black')

    plt.xticks(x+bar_width/2, tick_label)

    plt.legend(loc = 4)
    plt.xlabel("($c$)")
    plt.ylabel("运行时间($ms$)")
    plt.title("计算$\epsilon$的运行时间(优化后)")

    plt.tight_layout()

    plt.subplot(2,2,4)

    t3 = [4,6,26,221]

    bar_width = 0.35

    tick_label = ["1", "50", "500","5000（次）"]
    x = np.arange(len(tick_label))



    plt.bar(x, t3, bar_width, align="center", color="seashell", label="Adult", alpha=0.5, edgecolor='black')

    plt.xticks(x, tick_label)

    plt.legend(loc = 4)
    plt.xlabel("($d$)")
    plt.ylabel("运行时间($ms$)")
    plt.title("不同查询次数下计算$\epsilon$的运行时间(优化后)")

    plt.tight_layout()


    plt.savefig("../img/compared_time.png")

    plt.show()

_plot_time()
