import pandas as pd
import folium
from folium.plugins import MarkerCluster

loc_data = pd.read_csv("../data/locs.csv")

loc = loc_data["locid"].tolist()
lat = loc_data["latitude"].tolist()
lon = loc_data["longitude"].tolist()

loc = set(loc)

print(len(loc))


m = folium.Map(location=[39.91, 116.40], #地图中心点
               zoom_start=12,            #初始地图等级
               #腾讯地图瓦片
    tiles='http://rt1.map.gtimg.com/realtimerender?z={z}&x={x}&y={-y}&type=vector&style=6',
               #默认参数
    attr='default')
#创建聚合
marker_cluster =MarkerCluster().add_to(m)
#for循环添加标记点
for i in range(len(loc_data)):
    folium.Marker(location=[lat[i], lon[i]],  #坐标用[纬度，经度]
                  # popup=folium.Popup(data.loc[i,'小区名'],
                  #                    parse_html=True,
                  #                    max_width=100)                #提示语横向完全显示
                 ).add_to(marker_cluster)

m.save('location.html')
