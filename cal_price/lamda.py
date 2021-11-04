import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve
from numpy.random import random
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

# 关于lamda的概率函数
'''
lamda越大，相应的概率越大，eps越小
即X越大，eps越小
'''
def plot_X():
    x = [i*0.01 for i in range(1,100)]
    y = []

    for i in x:
        y.append((i-1)/(1+i) * (i / np.log(i)))


    plt.plot(x,y)
    plt.show()
# plot_X()


'''
lamda越小，eps越大，添加的噪声越小
lamda越大，eps越小，添加的噪声越大
'''

def plot_lamda():
    eps = [i*0.01 for i in range(1,1000)]
    lamda = []
    for e in eps:
        lamda.append(np.e ** (-e))
    plt.plot(eps,lamda)

    plt.show()

# plot_lamda()

def calP(n, p):
    count = 0
    total = n
    epsList = list()
    for k in range(n + 1):
        count += 1
        acc = -1 * p
        x = symbols('x')
        N = 2 * k + 1
        for i in range(1, k + 2):
            tmp = comb(N, k + i) * (1 - x) ** (k + i) * (x ** (k + 1 - i))
            acc += tmp

        res = solve(acc, x)

        eps = list()

        for r in res:
            try:
                e = np.e ** cmath.log(r)
                if e.real >= 0:
                    eps.append(round(e.real,2))
            except Exception as e:
                print(e)
                continue

        # print(eps)

        epsList.append(min(eps))


    plt.plot(epsList, marker = '^')
    plt.xlabel("t")
    plt.ylabel("epsilon")
    plt.title("epsilon within t")

    plt.show()

    print(epsList)


calP(3, 0.8)