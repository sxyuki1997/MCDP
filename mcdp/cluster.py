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
    lat.append(round(float(item[1]),5))
    lon.append(round(float(item[0]),5))

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

y_pred=KMeans(n_clusters=50,random_state=9).fit_predict(X)
plt.scatter(lon,lat,c=y_pred)
plt.title("聚类后位置点的分布（$k=50$）")
plt.xlabel("经度（longitude）")
plt.ylabel("维度（latitude）")

plt.tight_layout()


plt.show()


#使用Calinski-Harabasz Index评估
# print(metrics.calinski_harabaz_score(X,y_pred))
