import numpy as np
import pandas as pd

loc_data = pd.read_csv("../data/shanghai_locs.csv")

all_locs = loc_data['locid'].tolist()
all_time = loc_data['time'].tolist()
all_users = loc_data['userid'].tolist()

# 按月划分
monthlist = ['01','02','03','04','05','06','07','08','09','10','11','12']
locList = []

user_month = []


for month in monthlist:
    user_month_corr = []
    user_corr_matrix = []
    users=[]
    locs = []
    times = []
    user_corr = []
    monthtmp = []

    for i in range(len(loc_data)):
        if str(all_time[i])[0:8] == "'2009-" + month:
            monthtmp.append([int(all_users[i]), all_locs[i], all_time[i]])

    for item in monthtmp:
        users.append(item[0])
        locs.append(item[1])
        times.append(item[2])

    locs = set(locs)
    times = set(times)
    users = set(users)

    print(str(month) + "月数据：=====================")
    print("时间区间：",len(times))
    print("用户数量：", len(users))
    print("地点数量：", len(locs))

    # 获取用户之间的关联
    print("用户关联情况：")
    # 所有用户关联表
    user_corr = np.load("user_corr.npy")

    # 查找用户的关联
    for k in range(len(user_corr)):
        useri = int(user_corr[k][0])
        userj = int(user_corr[k][1])

        if useri in users and userj in users:
            user_month_corr.append([useri, userj])
            print([useri, userj])

    # 构造关联矩阵


