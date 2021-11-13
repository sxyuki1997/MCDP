import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(6, 5))

def plot_degree():
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 20, 21, 24, 25, 26, 28, 29, 30, 31, 32, 36, 38, 47, 49,
     54]
    freq = [16, 9, 9, 15, 5, 4, 2, 3, 3, 3, 7, 2, 5, 2, 1, 2, 1, 1, 2, 2, 3, 1, 1, 2, 2, 4, 1, 1, 1, 1, 1, 1]
    plt.scatter(d,freq)
    plt.grid()
    plt.xlabel("度")
    plt.ylabel("频率")
    plt.title("用户社交关联图度的分布")
    plt.show()

plot_degree()