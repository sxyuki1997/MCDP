import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import folium
from folium.plugins import MarkerCluster


plt.rcParams['font.sans-serif'] = ['STZhongsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10, 4))


X = np.load("originallocs.npy")
print("位置个数：", len(X))




# X,y=make_blobs(n_samples=1000,n_features=2,centers=[[-1,-1],[0,0],[1,1],[2,2]],cluster_std=[0.4,0.2,0.2,0.2],random_state=9)
# print(X)
# print(X[:,0])
lat = []
lon = []
for item in X:
    lat.append(round(float(item[1]),8))
    lon.append(round(float(item[0]),8))

def _cluster_check():

    #使用Calinski-Harabasz Index评估
    # print(metrics.calinski_harabaz_score(X,y_pred))

    maxs = 0
    k = 0
    ss = []
    interia = []
    mink = 45
    maxk = 66

    for i in range(mink, maxk):
        model_kmeans = KMeans(n_clusters=i, random_state=9)
        y_pred = model_kmeans.fit_predict(X)
        s = metrics.silhouette_score(X,y_pred,metric='euclidean')
        inter = model_kmeans.inertia_
        interia.append(inter)
        ss.append(s)
        if (maxs <= s):
            maxs = s
            k = i
        # print(s)  #轮廓系数
    print(k)


    plt.figure(figsize=(10, 4))

    plt.subplot(1,2,1)
    x = [i for i in range(mink, maxk)]
    plt.plot(x, ss, marker='^', label="轮廓系数")
    plt.xlabel("k")
    plt.ylabel("轮廓系数")
    plt.title("不同的k值选取与轮廓系数")
    plt.legend()
    plt.tight_layout()
    # plt.show()

    plt.subplot(1,2,2)
    x = [i for i in range(mink,maxk)]
    plt.plot(x, interia, marker='o', label = "SSE")
    plt.xlabel("k")
    plt.ylabel("簇内误方差和（SSE）")
    plt.title("不同的k值选取与SSE")
    plt.legend()
    plt.tight_layout()
    plt.show()



plt.figure(figsize=(10, 4))
# 绘制聚类图
plt.subplot(1,2,1)
plt.grid()

plt.scatter(lon, lat)
plt.title("聚类前位置点的分布")
plt.xlabel("经度（longitude）")
plt.ylabel("维度（latitude）")
# plt.scatter([1,2,3], [4,5,6])
# plt.scatter(X[:,0],X[:,1])
# plt.show()
plt.tight_layout()

plt.subplot(1,2,2)
#选择聚类数K=4
plt.grid()


# 进行聚类计算
cluster_num=65
y_pred = KMeans(n_clusters=cluster_num, random_state=9).fit_predict(X)
print("==========聚类簇=========")
print(y_pred)

cluster_loc = []

for i in range(len(y_pred)):
    cluster_loc.append([lon[i], lat[i], y_pred[i]])

np.save("cluster_loc.npy", cluster_loc)

plt.scatter(lon,lat,c=y_pred)
plt.title("聚类后位置点的分布（" + "$k=$"+ str(cluster_num) +"）")
plt.xlabel("经度（longitude）")
plt.ylabel("维度（latitude）")

plt.tight_layout()

# plt.show()

def plot_map_cluster():
    # 在地图上标出
    '''创建底层Map对象'''
    m = folium.Map(location=[0.5, 100.5],
                   zoom_start=8,
                   control_scale=True)

    # [lat, lon]
    colorlist = ['beige', 'darkgreen', 'darkpurple', 'blue', 'cadetblue', 'darkblue',
                 'red', 'black', 'gray', 'darkred', 'lightred', 'green', 'orange', 'lightgray',
                 'beige', 'darkgreen', 'darkpurple', 'blue', 'cadetblue', 'darkblue',
                 'red', 'black', 'gray', 'darkred', 'lightred', 'green', 'orange', 'lightgray',
                 'beige', 'darkgreen', 'darkpurple','blue', 'cadetblue', 'darkblue',
                 'red', 'black', 'gray', 'darkred', 'lightred', 'green', 'orange', 'lightgray',
                 'beige', 'darkgreen', 'darkpurple',  'blue', 'cadetblue', 'darkblue',
                 'red', 'black', 'gray', 'darkred', 'lightred', 'green', 'orange', 'lightgray',
                 'beige', 'darkgreen', 'darkpurple',   'blue', 'cadetblue', 'darkblue',
                 'red', 'black', 'gray', 'darkred', 'lightred', 'green', 'orange', 'lightgray'
                 ]


    for i in range(len(lat)):
        folium.Marker(location=[lat[i], lon[i]],
                      # icon=folium.Icon(color=colorlist[y_pred[i]], prefix='glyphicon')
                      ).add_to(m)
    '''显示m'''
    m.save('cluster_loc_origin.html')






