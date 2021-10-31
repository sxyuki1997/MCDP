import pandas as pd
import numpy as np

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
    types = [demographics, health, properties, activity, activity, consumer]
    w = [0, 0, 0, 0, 0]
    for i in range(len(types)):
        for attr in attrList:
             if attr in types[i]:
                 w[i] += 1
    _sum = sum(w)
    for i in range(len(w)):
        w[i] = w[i] / _sum
    return w
                 
def main():
    data_url = "../data/income.csv"
    A = _attr_extraction(data_url)
    W = _cal_type_weight(A)
    # 数据类型价值矩阵
    C = [0.3685, 0.6725, 0.19, 0.0825, 0.07]
    p = sum(np.array(W) * np.array(C))

    print(p)
    

main()
