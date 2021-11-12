import pandas as pd
import folium
from folium.plugins import MarkerCluster

loc_data = pd.read_csv("../data/locs.csv")

loc = loc_data["locid"].tolist()
lat = loc_data["latitude"].tolist()
lon = loc_data["longitude"].tolist()

# loc = set(loc)
#
# print(len(loc))

coor = []
for i in range(len(lat)):
    coor.append([lon[i], lat[i]])


#
# m = folium.Map(location=[39.91, 116.40], #地图中心点
#                zoom_start=12,            #初始地图等级
#                #腾讯地图瓦片
#     # tiles='http://rt1.map.gtimg.com/realtimerender?z={z}&x={x}&y={-y}&type=vector&style=6',
#     #            #默认参数
#     attr='default')
# #创建聚合
# marker_cluster =MarkerCluster().add_to(m)
# #for循环添加标记点
# # for i in range(len(loc_data)):
# folium.Marker(location=[30, 120],  #坐标用[纬度，经度]
#               # popup=folium.Popup(data.loc[i,'小区名'],
#               #                    parse_html=True,
#               #                    max_width=100)                #提示语横向完全显示
#              ).add_to(marker_cluster)
#
# m.save('location.html')


'''创建底层Map对象'''
m = folium.Map(location=[0.5,100.5],
              zoom_start=8,
              control_scale=True)

#创建聚合
marker_cluster =MarkerCluster().add_to(m)
'''定义geojson图层'''
gj = folium.GeoJson(data={ "type": "MultiPoint",
  "coordinates": coor
  })

'''为m添加geojson层'''
gj.add_to(marker_cluster)

'''显示m'''
m.save('location.html')
