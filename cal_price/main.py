import pandas as pd
import numpy as np
import time

# 属性集提取
def _attr_extraction(data):
    attrList = pd.read_csv(data, nrows=0).columns
    return attrList

# 贝叶斯多分类，计算属性集属于各个数据类型的权重
def _cal_type_weight(attrList):
    # 利用map，达到O(1)
    demographics = {"age", "work", "education", "marital", "occupation", "relationship", "race", "sex",
                    "nationality"}
    health = {"height", "weight", "vision", "fat"}
    properties = {"income", "salary", "capital", "stock"}
    activity = {"location"}
    consumer = {"buy_item"}
    types = [demographics, health, properties, activity, consumer]
    w = [0, 0, 0, 0, 0]
    for i in range(len(types)):
        for attr in attrList:
             if attr in types[i]:
                 w[i] += 1
    _sum = sum(w)
    for i in range(len(w)):
        w[i] = w[i] / _sum
    return w

# 目标属性集占所有属性的比重，通过信息熵来确定，每个属性下所含的信息熵
# 目标属性信息熵 / 总的数据集的信息熵

def _cal_entropy(data, targetA, A):
    A = A.tolist()
    h = [0 for i in range(len(A))]
    t = []
    sum_t_h = 0
    for attr in targetA:
        t.append(A.index(attr))

    for a in range(len(A)):
        tmp = data[A[a]].tolist()
        n = len(tmp)
        for i in tmp:
            pr = tmp.count(i) / n
            h[a] += - pr * np.log(pr)

    for i in t:
        sum_t_h += h[i]

    hw = sum_t_h / sum(h)

    print(hw)
    return hw


                 
def main():
    data_url = "../data/income.csv"
    data = pd.read_csv(data_url)
    # 开始时间
    startT = time.time()*1000 #毫秒数
    A = _attr_extraction(data_url)
    # 权重计算
    W = _cal_type_weight(A)
    # 数据类型价值矩阵
    C = [0.3685, 0.6725, 0.19, 0.0825, 0.07]
    p = sum(np.array(W) * np.array(C))
    # 可信度设置
    c = 0.9
    p = p * c
    # 时效性设置
    t0 = 0
    tc = 0
    T = tc-t0
    delta = 1 / ((1+0.05)**T)
    p = p*delta
    # 信息熵计算
    hw = _cal_entropy(data, ['age', 'income'], A)
    p = p*hw

    endT = time.time() * 1000
    interval = endT - startT
    print(interval)
    print(p)

main()
