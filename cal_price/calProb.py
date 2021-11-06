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
def calc_ent(x):
    """
        calculate shanno ent of x
    """
    x = np.array(x)
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        logp = np.log2(p)
        ent -= p * logp

    return ent

# x = np.array([1,0,1,0,1,0,1])
# print(calc_ent(x))

def _cal_entropy(data, targetA, A):
    A = A.tolist()
    h = [0 for i in range(len(A))]
    t = []
    sum_t_h = 0
    for attr in targetA:
        t.append(A.index(attr))

    for a in range(len(A)):
        tmp = data[A[a]].tolist()
        ent = calc_ent(tmp)
        h[a] = ent

    for i in t:
        sum_t_h += h[i]

    hw = sum_t_h / sum(h)

    print("属性权重因子hw：",hw)
    print("信息熵矩阵h：", h)
    return hw

# 计算攻击成功概率
def _cal_attack_p(p):
    # 拟合曲线
    prob = 0.84 * np.e**(-2.44*p) + 0.13
    return prob

class CalProbability(object):

    def __init__(self, data_url, targetA):
        self.data_url = data_url
        self.targetA = targetA


    def _cal_prob(self):
        n = 5000
        data_url = self.data_url
        # data_url = "../data/adult_2.csv"
        data = pd.read_csv(data_url)
        # 开始时间
        startT = time.time() #毫秒数
        A = _attr_extraction(data_url)
        C = [0.3685, 0.6725, 0.19, 0.0825, 0.07]

        for i in range(n):
            # 权重计算
            W = _cal_type_weight(A)
            # 数据类型价值矩阵
            p = sum(np.array(W) * np.array(C))
            # 可信度设置
            c = 0.9
            p = p * c
            # 时效性设置
            t0 = 0
            tc = 5
            T = tc-t0
            delta = 1 / ((1+0.05)**T)
            p = p*delta

        endT = time.time()
        interval = endT - startT
        print("=====优化后运行时间=======：", interval * 1000)
        # 信息熵计算
        hw = _cal_entropy(data, self.targetA, A)
        p = p*hw
        prob = _cal_attack_p(p)
        print("数据价值：",p)
        print("攻击成功概率", prob)
        # endT = time.time()
        # interval = endT - startT
        # print("优化前运行时间：", interval * 1000)
        return prob


# 计算相应的攻击成功概率
heart_data_url = '../data/heart.csv' #2018年
income_data_url = '../data/adult_2.csv' #2016年
prob = CalProbability(heart_data_url, ['age', 'target'])._cal_prob()
print(prob)

# adult 0.86 0.3
# heart 0.88 0.26