import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 600
plt.rcParams['figure.figsize'] = (6,5)

label = ["随机森林", "决策树", "逻辑回归", "朴素贝叶斯"]

def _plot_attack_acc():
    x = np.arange(3)

    y = [0.96, 1.00, 0.91]
    y1 = [0.94, 1.00, 0.88]

    bar_width = 0.35
    tick_label = ["所有攻击", "差分攻击", "语义攻击"]

    plt.bar(x, y, bar_width, align="center", label="Adult", alpha=0.5, color="seashell", edgecolor='black')
    plt.bar(x + bar_width, y1, bar_width, align="center", label="Credit", alpha=0.5, color="dimgrey", edgecolor='black')

    plt.ylabel("准确度")

    plt.xticks(x + bar_width / 2, tick_label)

    # 标注数值
    # for x, y in enumerate(y):
    #     plt.text(x, y, '%s' % y, ha='center')
    #
    # for x, y1 in enumerate(y1):
    #     plt.text(x + bar_width, y1, '%s' % y1, ha='center')

    plt.title("检测准确度")
    plt.legend(loc=4)
    plt.savefig("../img/accFinal.png")
    plt.show()

# _plot_attack_acc()

def _plot_origin_running_time():
    t1 = [200, 216, 257, 699, 6338]
    t2 = [1, 1, 4, 25, 204]
    t3 = [5, 6, 14, 38, 249]
    t4 = [2, 2, 4, 4, 29]

    plt.subplot(2, 1, 1)

    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(t1, label="随机森林", marker='s', linewidth=1)

    plt.legend()
    plt.title("各分类算法运行时间")
    plt.ylabel("运行时间($ms$)")

    plt.subplot(2, 1, 2)
    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(t2, label="决策树", marker='*', color="orange", linewidth=1)
    plt.plot(t3, label="逻辑回归", marker='p', color="green", linewidth=1)
    plt.plot(t4, label="朴素贝叶斯", marker='^', color="red", linewidth=1)

    plt.legend()
    plt.ylabel("运行时间($ms$)")
    plt.xlabel("数据集大小")
    plt.savefig("../img/origin_running_time.png")

    plt.show()

# _plot_origin_running_time()

def _plot_advanced_running_time():
    t1 = [18, 16, 28, 56, 529]
    t2 = [1, 1, 4, 25, 204]
    t3 = [5, 6, 14, 38, 249]
    t4 = [2, 2, 4, 4, 29]
    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(t1, label="随机森林", marker='s', linewidth=1)
    plt.plot(t2, label="决策树", marker='*', linewidth=1)
    plt.plot(t3, label="逻辑回归", marker='p', linewidth=1)
    plt.plot(t4, label="朴素贝叶斯", marker='^', linewidth=1)
    plt.legend()
    plt.title("各分类算法运行时间（优化后）")
    plt.ylabel("运行时间($ms$)")
    plt.xlabel("数据集大小")
    plt.savefig("../img/advanced_running_time.png")

    plt.show()

_plot_advanced_running_time()

def _plot_acc_fscore():
    plt.rcParams['figure.figsize'] = (10, 4)

    plt.subplot(1,2,1)
    s1 = [0.33, 0.90, 0.95, 0.95, 0.95]
    s2 = [0.33, 0.80, 0.89, 0.88, 0.88]
    s3 = [0.33, 0.86, 0.91, 0.91, 0.90]
    s4 = [0.33, 0.66, 0.77, 0.77, 0.76]

    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(s1, label="随机森林", marker='s', linewidth=1)
    plt.plot(s2, label="决策树", marker='*', linewidth=1)
    plt.plot(s3, label="逻辑回归", marker='p', linewidth=1)
    plt.plot(s4, label="朴素贝叶斯", marker='^', linewidth=1)
    plt.legend()
    plt.title("各分类算法的Accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("数据集大小")
    plt.tight_layout()
    plt.subplot(1,2,2)

    s1 = [0.00, 0.92, 0.96, 0.97, 0.97]
    s2 = [0.00, 0.83, 0.92, 0.90, 0.90]
    s3 = [0.00, 0.89, 0.93, 0.93, 0.92]
    s4 = [0.00, 0.78, 0.85, 0.85, 0.85]

    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(s1, label="随机森林", marker='s', linewidth=1)
    plt.plot(s2, label="决策树", marker='*', linewidth=1)
    plt.plot(s3, label="逻辑回归", marker='p', linewidth=1)
    plt.plot(s4, label="朴素贝叶斯", marker='^', linewidth=1)
    plt.legend()
    plt.title("各分类算法的F1-Score")
    plt.ylabel("F1-score")
    plt.xlabel("数据集大小")
    plt.savefig("../acc_f1_score.png")
    plt.tight_layout()
    plt.show()

# _plot_acc_fscore()

def _plot_normal_sql():
    plt.rcParams['figure.figsize'] = (10, 3)


    plt.subplot(1,3,1)
    s1 = [0.33, 0.91, 0.91, 0.90, 0.90]
    s3 = [0.33, 0.83, 0.86, 0.85, 0.84]

    plt.xticks([0, 1, 2, 3, 4], [10, 100, 1000, 10000, 100000])
    plt.plot(s1, label=label[0], marker='s')
    plt.plot(s3, label=label[2], marker='p', color="green")
    plt.legend()
    plt.title("正常SQL查询的Precision")
    plt.ylabel("Precision")
    plt.xlabel("数据集大小")
    plt.tight_layout()

    plt.subplot(1,3,2)
    s1 = [1.00, 0.83, 0.95, 0.99, 0.99]
    s3 = [1.00, 0.83, 0.89, 0.90, 0.89]

    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(s1, label=label[0], marker='s')
    plt.plot(s3, label=label[2], marker='p',color="green")
    plt.legend()
    plt.title("正常SQL查询的Recall")
    plt.ylabel("Recall")
    plt.xlabel("数据集大小")

    plt.tight_layout()


    plt.subplot(1,3,3)

    s1 = [0.50, 0.87, 0.93, 0.94, 0.94]
    s3 = [0.50, 0.83, 0.88, 0.87, 0.86]

    plt.xticks([0, 1, 2, 3, 4],
               [10, 100, 1000, 10000, 100000])
    plt.plot(s1, label=label[0], marker='s', linewidth=1)
    plt.plot(s3, label=label[2], marker='p', linewidth=1, color="green")
    plt.legend()
    plt.title("正常SQL查询的F1-score")
    plt.ylabel("F1-score")
    plt.xlabel("数据集大小")
    plt.tight_layout()

    plt.savefig("../img/normal_sql.png")

    plt.show()



# _plot_normal_sql()
