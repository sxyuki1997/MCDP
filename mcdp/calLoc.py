import pandas as pd
import folium
from folium.plugins import MarkerCluster
import time
import numpy as np

loc_data = pd.read_csv("../data/locs.csv")
user_data = pd.read_csv("../data/userEdge.csv")
n = len(loc_data)

userid = loc_data['userid'].tolist()
loc = loc_data["locid"].tolist()
lat = loc_data["latitude"].tolist()
lon = loc_data["longitude"].tolist()
# useri = user_data["useri"].tolist()
# userj = user_data["userj"].tolist()

filename = "../data/Brightkite_totalCheckins.txt"
user_filename = "../data/Brightkite_edges.txt"

read1 = [i for i in range(1000000)]
read2 = [i for i in range(1000000, 2000000)]
read3 = [i for i in range(2000000, 3000000)]
read4 = [i for i in range(3000000, 4000000)]

loctxt1 = []
loctxt2 = []
loctxt3 = []
loctxt4 = []

def data_clean(read, dataset):
    with open(filename, 'r') as file_to_read:
        lines = file_to_read.readlines() # 整行读取数据
        for i in read:
            tmp = lines[i].split()
            print("==========运行中，第" + str(i) + "条数据" + "/4000000")
            dataset.append(tmp)  # 添加新读取的数据

# st = time.time()
# data_clean(read1, loctxt1)
# np.save("loctxt1.npy", loctxt1)
# data_clean(read2, loctxt2)
# np.save("loctxt2.npy", loctxt2)
# data_clean(read3, loctxt3)
# np.save("loctxt3.npy", loctxt3)
# data_clean(read4, loctxt4)
# np.save("loctxt4.npy", loctxt4)
# et = time.time()
# print("解析4,000,000条数据的时间（s）：", et - st)


def data_user_clean(filename):
    users = []
    with open(filename, 'r') as file_to_read:
        lines = file_to_read.readlines() # 整行读取数据
        for i in range(len(lines)):
            tmp = lines[i].split()
            print("==========运行中，第" + str(i) + "条数据/" + str(len(lines)))
            users.append(tmp)  # 添加新读取的数据
    np.save("users.npy", users)
    return users

# data_user_clean(user_filename)


def plot_map(lat, lon):
    # 地图展示
    m = folium.Map(location=[30, 120], #地图中心点
                   zoom_start=12,            #初始地图等级
                   #腾讯地图瓦片
        tiles='http://rt1.map.gtimg.com/realtimerender?z={z}&x={x}&y={-y}&type=vector&style=6',
                   #默认参数
        attr='default')
    #创建聚合
    marker_cluster =MarkerCluster().add_to(m)
    #for循环添加标记点
    for i in range(len(lat)):
        folium.Marker(location=[lat[i], lon[i]],  #坐标用[纬度，经度]
                      # popup=folium.Popup(data.loc[i,'小区名'],
                      #                    parse_html=True,
                      #                    max_width=100)                #提示语横向完全显示
                     ).add_to(marker_cluster)

    m.save('location.html')



# 提取中国地区的数据
# 经度范围：73°33′E至135°05′E；纬度范围：3°51′N至53°33′N。
# 上海的经纬度是东经120°52′-122°12′，北纬30°40′-31°53′之间。
# lat >= 30.4 and lat <= 31.53 and lon>=121 and lon <= 122.12 (上海市)
def extract_china_data():
    china_loc_data = []
    users = []
    locs = []
    clat = []
    clon = []
    user_corr = []


    # 获取2010年的数据,上海
    loctxt1 = np.load("loctxt1.npy")
    loctxt2 = np.load("loctxt2.npy")
    loctxt3 = np.load("loctxt3.npy")
    loctxt4 = np.load("loctxt4.npy")

    locList = [loctxt1, loctxt2, loctxt3, loctxt4]

    for data in locList:
        for i in range(len(data)):
            if len(data[i]) == 5:
                lat = float(data[i][2])
                lon = float(data[i][3])
                userid = data[i][0]
                locid = data[i][4]
                time = data[i][1]
                if lat >= 31.2 and lat <= 31.3 and lon>=121.4 and lon <= 122\
                        and str(time)[0:4] == '2009':
                    china_loc_data.append([userid, lat, lon, locid, time])
                    print([userid, lat, lon, locid, time])

    for item in china_loc_data:
        users.append(item[0])
        locs.append(item[3])
        clat.append(item[1])
        clon.append(item[2])

    users = set(users)
    locs = set(locs)

    print("users集合：", users)
    print("locs集合", locs)
    print("位置数据集大小：", len(china_loc_data))
    print("用户数量：", len(users))
    print("位置数量：", len(locs))

    plot_map(clat, clon)

    # 获取用户之间的关联
    print("====用户关联======")
    # 所有用户关联表
    users_map = np.load("users.npy")

    # 查找用户的关联
    for k in range(len(users_map)):
        useri = users_map[k][0]
        userj = users_map[k][1]
        # print("=====executing: " + str(k) + "/" + str(len(users_map)) + "======")

        if useri in users and userj in users:
            user_corr.append([useri, userj])

    for item in user_corr:
        print(item)
    np.save("user_corr.npy", user_corr)


extract_china_data()
