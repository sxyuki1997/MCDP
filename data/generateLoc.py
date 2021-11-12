import numpy as np
import pandas as pd

# loc_data = pd.read_csv("../data/shanghai_locs.csv")
loc_data = np.load("japan_data.npy")
# [userid, lat, lon, locid, time]
all_locs = []
all_time = []
all_users = []
all_lat = []
all_lon = []

for item in loc_data:
    all_users.append(item[0])
    all_lat.append(item[1])
    all_lon.append(item[2])
    all_locs.append(item[3])
    all_time.append(item[4])

# 按月划分
monthlist = ['01-01','02-01','03-01','04-01','05-01','06-01','07-01','08-01','09-01','10-01','11-01','12-01']
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
        if str(all_time[i])[0:10] == "2009-" + month:
            monthtmp.append([all_users[i], all_locs[i], all_time[i]])

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
        useri = user_corr[k][0]
        userj = user_corr[k][1]

        if useri in users and userj in users:
            user_month_corr.append([useri, userj])
            print([useri, userj])
