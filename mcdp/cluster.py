import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np


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

cluster_num=76
y_pred = KMeans(n_clusters=cluster_num, random_state=9).fit_predict(X)

plt.scatter(lon,lat,c=y_pred)
plt.title("聚类后位置点的分布（" + " ($k$="+ str(cluster_num) +"）")
plt.xlabel("经度（longitude）")
plt.ylabel("维度（latitude）")

plt.tight_layout()


plt.show()


#使用Calinski-Harabasz Index评估
# print(metrics.calinski_harabaz_score(X,y_pred))

maxs = 0
k = 0
ss = []
interia = []
for i in range(50, 81):
    model_kmeans = KMeans(n_clusters=i, random_state=9)
    y_pred = model_kmeans.fit_predict(X)
    s = metrics.silhouette_score(X,y_pred,metric='euclidean')
    inter = model_kmeans.inertia_
    interia.append(inter)
    ss.append(s)
    if (maxs <= s):
        maxs = s
        k = i
    print(s)  #轮廓系数
print(k)


plt.figure(figsize=(10, 4))

plt.subplot(1,2,1)
x = [i for i in range(50,81)]
plt.plot(x, ss, marker='^', label="轮廓系数")
plt.xlabel("k")
plt.ylabel("轮廓系数")
plt.title("不同的k值选取与轮廓系数")
plt.legend()
plt.tight_layout()
# plt.show()

plt.subplot(1,2,2)
x = [i for i in range(50,81)]
plt.plot(x, interia, marker='o', label = "SSE")
plt.xlabel("k")
plt.ylabel("簇内误方差和（SSE）")
plt.title("不同的k值选取与SSE")
plt.legend()
plt.tight_layout()
plt.show()
