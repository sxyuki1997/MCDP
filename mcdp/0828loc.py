import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import MarkerCluster


def plot_map_jap(coor):
    '''创建底层Map对象'''
    m = folium.Map(location=[0.5, 100.5],
                   zoom_start=8,
                   control_scale=True)

    # # 创建聚合
    # marker_cluster = MarkerCluster().add_to(m)
    '''定义geojson图层'''
    for item in coor:
        folium.Marker(location=[item[1], item[0]]).add_to(m)

    '''显示m'''
    m.save('loc0001.html')


plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(12, 15))


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
timelist = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17',
            '18','19','20','21','22','23']
locList = []

user_month = []
datemax = ""

def graph_plot(users, user_corr, title):
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

    ax = plt.gca()
    ax.set_title(title)
    # nx.draw(G, with_labels=False, node_color='navy', edge_color="silver",node_size=80)
    nx.draw(G, pos = nx.random_layout(G), with_labels=True, node_color='royalblue', edge_color="dimgrey")

    # plt.title("部分用户社交关联图")
    # plt.show()


for t in range(0, len(timelist)-1, 2):
    print("=========时刻："+timelist[t]+"=============")
    loc_cnt_map = {}

    user_month_corr = []
    user_corr_matrix = []
    users = []
    locs = []
    times = []
    user_corr = []
    monthtmp = []
    lats = []
    lons = []
    coor = []

    for i in range(len(loc_data)):
        if (str(all_time[i])[0:13] == "2009-08-28T" + timelist[t]) or (str(all_time[i])[0:13] == "2009-08-28T" + timelist[t+1]):
            monthtmp.append([all_users[i], all_locs[i], all_time[i], all_lat[i], all_lon[i]])
            # print([all_users[i], all_locs[i], all_time[i], all_lat[i], all_lon[i]])

    for item in monthtmp:
        users.append(item[0])
        locs.append(item[1])
        times.append(item[2])
        lats.append(item[3])
        lons.append(item[4])

    # np.save("locdata0801.npy", monthtmp)

    for loc in locs:
        if loc not in loc_cnt_map:
            loc_cnt_map[loc] = 1
        else:
            loc_cnt_map[loc] += 1

    setlocs = set(locs)
    times = set(times)
    setusers = set(users)

    print("****************数据表信息：******************")
    print("时间区间：", len(times))
    print("用户数量：", len(setusers))
    print("地点数量：", len(locs))
    print("数据集大小：", len(monthtmp))
    print("位置统计：")
    for key in loc_cnt_map:
        print(key, loc_cnt_map[key])

    for i in range(len(locs)):
        locList.append([lons[i],lats[i],locs[i]])


    # # 获取用户之间的关联
    # print("用户关联情况：")
    # # 所有用户关联表
    # user_corr = np.load("user_corr.npy")
    #
    # # 查找用户的关联
    # for k in range(len(user_corr)):
    #     useri = user_corr[k][0]
    #     userj = user_corr[k][1]
    #
    #     if useri in users and userj in users:
    #         user_month_corr.append((useri, userj))
            # print((useri, userj))
    # np.save("user_corr_0828.npy", user_month_corr)
    # plt.subplot(4,3,t/2+1)
    #
    # graph_plot(users, user_month_corr,"时刻区间" + str(t) + "-" + str(t+1) + "用户关联")

# plt.show()
plot_map_jap(locList)


def plot_degree():
    # 计算度
    degree_map = {}
    for item in user_month_corr:
        if item[0] not in degree_map:
            degree_map[item[0]] = 1
        else:
            degree_map[item[0]] += 1
    degree = []
    for key in degree_map:
        degree.append(degree_map[key])
        print(degree_map[key])

    degree_set = set(degree)
    print(degree_set)

    degree_cnt = []
    for i in degree_set:
        degree_cnt.append(degree.count(i))

    print(degree_cnt)

    print(degree_map)
    # d = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 23, 24, 26, 28, 29, 33, 36, 37, 41, 46]
    # freq = [12, 2, 6, 11, 10, 6, 8, 4, 2, 2, 3, 3, 2, 3, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]

# plot_degree()