import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

G=nx.Graph()
filename="F:\\git\\NRP\\soc-pokec-relationships.txt"
#filename="F:\\git\\NRP\\test.txt"
edges = pd.read_table(filename, header=None, sep='\n')
for i in range(30622564):
    coordinate = edges[0][i].split()
    G.add_edge(coordinate[0],coordinate[1])
print(G.number_of_nodes())
nx.draw(G)
plt.show()
