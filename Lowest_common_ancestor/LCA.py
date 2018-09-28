import networkx as nx

#Start functions
def lowest_common_ancestor(graph, a, b):
    print("here")
    holdA = ''
    holdB = ''
    countA = 0
    countB = 0
    i = 0

    holdA = a
    while(holdA != None):
        countA += 1
        holdA = (G.predecessors(holdA)).next()

    holdB = b
    while(holdB != None):
        countB += 1
        holdB = (G.predecessors(holdB)).next()
#End functions


G = nx.DiGraph()
G.add_nodes_from(['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p'])
G.add_edges_from([('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('c','g'),('d','h'),
                    ('d','j'),('e','k'),('e','l'),('f','m'),('g','o'),('h','i'),('m','n'),('o','p'),])

print ("Nodes: " + str(G.nodes))
print ("Edges: " + str(G.edges))

lowest_common_ancestor(G, 'p', 'i')
