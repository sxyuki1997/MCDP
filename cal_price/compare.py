import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 600
plt.rcParams['figure.figsize'] = (10,3)

ACC: [0.82, 0.81, 0.82]


lapalce_acc = [0.82, 0.81, 0.80]
geo_acc = [0.80,0.83,0.80]

laplace_w = [0.65, 0.77, 1.0]
geo_w = [1.32, 1.08, 1.26]

laplace_mse= [1.4, 0.88, 2.55]
geo_mse = [2.11,2.91,2.42]


x = np.arange(3)
bar_width = 0.35

tick_label = ["10", "15", "20"]

plt.subplot(1,3,1)


plt.bar(x, lapalce_acc, bar_width, align="center", color="seashell", label="Laplace机制", alpha=0.5, edgecolor='black')
plt.bar(x+bar_width, geo_acc, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

plt.xticks(x+bar_width/2, tick_label)

plt.legend(loc = 4)

plt.xlabel("直方图桶数")
plt.ylabel("平均精度")
plt.title("数据平均精度对比")
plt.subplots_adjust(wspace=0.3)
plt.tight_layout()

plt.subplot(1,3,2)

plt.bar(x, laplace_mse, bar_width, align="center", color="seashell", label="Laplace机制", alpha=0.5, edgecolor='black')
plt.bar(x+bar_width, geo_mse, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

plt.xticks(x+bar_width/2, tick_label)

plt.legend(loc = 4)

plt.xlabel("直方图桶数")
plt.ylabel("MSE")
plt.title("数据MSE对比")
plt.subplots_adjust(wspace=0.3)
plt.tight_layout()

plt.subplot(1,3,3)

plt.bar(x, laplace_w, bar_width, align="center", color="seashell", label="Laplace机制", alpha=0.5, edgecolor='black')
plt.bar(x+bar_width, geo_mse, bar_width,  align="center",color="dimgrey", label="Geo机制", alpha=0.5, edgecolor='black')

plt.xticks(x+bar_width/2, tick_label)

plt.legend(loc = 4)

plt.xlabel("直方图桶数")
plt.ylabel("w距离")
plt.title("直方图加噪前后分布差异对比")
plt.tight_layout()


plt.savefig("../img/compared_heart_acc.png")
plt.show()