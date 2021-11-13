import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 8))


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
monthlist = ['01','02','03','04','05','06','07','08','09','10','11','12']
datelist = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17',
            '18','19','20','21','22','23','24','25','26','27','28','29','30','31']
locList = []

user_month = []
datemax = ""

def graph_plot(users, user_corr):
    import networkx as nx
    import matplotlib.pyplot as plt
    import numpy as np

    nodes = []

    G = nx.Graph()

    for node in nodes:
        G.add_node(node)

    edges = user_corr


    r = G.add_edges_from(edges)

    # 计算最短路径。
    # shortest_way=nx.shortest_path(G,"F","D")
    # print(shortest_way)

    nx.draw(G, with_labels=False, node_color='navy', edge_color="silver",node_size=80)
    # plt.title("部分用户社交关联图")
    plt.show()

# for month in monthlist:
#     user_month_corr = []
#     user_corr_matrix = []
#     users=[]
#     locs = []
#     times = []
#     user_corr = []
#     monthtmp = []
#
#     for i in range(len(loc_data)):
#         if str(all_time[i])[0:10] == "2009-" + month:
#             monthtmp.append([all_users[i], all_locs[i], all_time[i]])
#
#     for item in monthtmp:
#         users.append(item[0])
#         locs.append(item[1])
#         times.append(item[2])
#
#     locs = set(locs)
#     times = set(times)
#     users = set(users)
#
#     print(str(month) + "月数据：=====================")
#     print("时间区间：",len(times))
#     print("用户数量：", len(users))
#     print("地点数量：", len(locs))
#
#     # 获取用户之间的关联
#     print("用户关联情况：")
#     # 所有用户关联表
#     user_corr = np.load("user_corr.npy")
#
#     # 查找用户的关联
#     for k in range(len(user_corr)):
#         useri = user_corr[k][0]
#         userj = user_corr[k][1]
#
#         if useri in users and userj in users:
#             user_month_corr.append([useri, userj])
#             print([useri, userj])
#



maxnums = 0

for month in monthlist:
    for date in datelist:

        user_month_corr = []
        user_corr_matrix = []
        users = []
        locs = []
        times = []
        user_corr = []
        monthtmp = []
        for i in range(len(loc_data)):
            if str(all_time[i])[0:10] == "2009-" + month + "-" + date:
                monthtmp.append([all_users[i], all_locs[i], all_time[i], all_lat[i], all_lon[i]])
                # print([all_users[i], all_locs[i], all_time[i], all_lat[i], all_lon[i]])

        for item in monthtmp:
            users.append(item[0])
            locs.append(item[1])
            times.append(item[2])

        # np.save("locdata0701.npy", monthtmp)


        locs = set(locs)
        times = set(times)
        setusers = set(users)

        print("============2009-" + month + "-" + date +"===========")

        print("时间区间：", len(times))
        print("用户数量：", len(setusers))
        print("地点数量：", len(locs))
        print("数据集大小：", len(monthtmp))

        if (len(monthtmp) >= maxnums):
            maxnums = len(monthtmp)
            datemax = "2009-" + month + "-" + date


print(datemax)



# 获取用户之间的关联
# print("用户关联情况：")
# 所有用户关联表
# user_corr = np.load("user_corr.npy")

# 查找用户的关联
# for k in range(len(user_corr)):
#     useri = user_corr[k][0]
#     userj = user_corr[k][1]
#
#     if useri in users and userj in users:
#         user_month_corr.append((useri, userj))
#         print((useri, userj))
# np.save("user_corr_0701.npy", user_month_corr)
# graph_plot(users, user_month_corr)

def plot_degree():
    # 计算度
    # degree_map = {}
    # for item in user_month_corr:
    #     if item[0] not in degree_map:
    #         degree_map[item[0]] = 1
    #     else:
    #         degree_map[item[0]] += 1
    # degree = []
    # for key in degree_map:
    #     degree.append(degree_map[key])
    #     print(degree_map[key])
    #
    # degree_set = set(degree)
    # print(degree_set)
    #
    # degree_cnt = []
    # for i in degree_set:
    #     degree_cnt.append(degree.count(i))
    #
    # print(degree_cnt)
    #
    # print(degree_map)
    d = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 23, 24, 26, 28, 29, 33, 36, 37, 41, 46]
    freq = [12, 2, 6, 11, 10, 6, 8, 4, 2, 2, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
