from scipy.optimize import root,fsolve
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt
import time

from sympy import symbols, solve

plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 600
plt.rcParams['figure.figsize'] = (6,5)


def _cal_attack_eps(prob, L, N):
    n = (N-1) / 2
    x = symbols('x')
    b = comb(N, n) * (1-x)**n * x ** (N-n) - prob

    res = solve(b, x)
    print(res[0])
    return float(res[0])



y = _cal_attack_eps(0.5, 1, 5)


def _solve_function(x):
    return (x-1)/(1+x) * (x / np.log(x)) + y


def plot_cross(y):
    x = [i*0.01 for i in range(700)]
    y1 = []
    y2 = []

    for i in x:
        y1.append(y)

    for i in x:
        if i == 0:
            y2.append(0)
        else:
            y2.append((i-1)/(1+i)/np.log(i)*i)

    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.show()


startT = time.time()  # 毫秒数

solved = root(_solve_function, [0.5])
endT = time.time()
interval = endT - startT
# 计算结果，lamda
print(solved.fun)
print(interval * 1000)
# print(-np.log(solved))

plot_cross(y)