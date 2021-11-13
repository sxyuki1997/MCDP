import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

user_corr = np.load("user_corr_0701.npy")

nodes=[]

G=nx.Graph()

for node in nodes:
    G.add_node(node)

edges=[
user_corr
]

r=G.add_edges_from(edges)

# 计算最短路径。
# shortest_way=nx.shortest_path(G,"F","D")
# print(shortest_way)

nx.draw(G, with_labels=True,node_color='y')

plt.show()