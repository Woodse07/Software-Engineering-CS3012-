import networkx as nx

#Start functions
def lowest_common_ancestor(graph, a, b):
    lca = None

    node_a_parents = set()
    finished = 0
    temp = a
    while(not finished):
        if(len(list(graph.predecessors(temp))) != 0):
            node = graph.predecessors(temp).next()
            node_a_parents.add(node)
            temp = node
        else:
            finished = 1
    print("Parents of node A: " + str(node_a_parents))

    node_b_parents = set()
    finished = 0
    temp = b
    while(not finished):
        if(len(list(graph.predecessors(temp))) != 0):
            node = graph.predecessors(temp).next()
            node_b_parents.add(node)
            temp = node
        else:
            finished = 1
    print("Parents of node B: " + str(node_b_parents))

    #Find first intersection in set #B
    intersec = node_a_parents.intersection(node_b_parents)
    while(bool(intersec)):
        lca = intersec.pop()

    print("Lowest common ancestor of " + a + " and " + b + " is: " + str(lca) + "!")
    return lca
#End functions
