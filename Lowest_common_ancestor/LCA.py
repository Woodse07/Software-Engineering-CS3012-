import networkx as nx

G = nx.Graph()
G.add_edge('A','B')
G.add_edge('B','C')
G.add_edge('C','D')
G.add_edge('D','A')
print (G)
