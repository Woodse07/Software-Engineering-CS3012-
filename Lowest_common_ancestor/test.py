import unittest
import networkx as nx
from LCA import lowest_common_ancestor

class myTest(unittest.TestCase):
    def test_general_lca(self):
        #Creating graph with networkx library..
        G = nx.DiGraph()
        #Adding random nodes..
        G.add_nodes_from(['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p'])
        #Adding random edges..
        G.add_edges_from([('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('c','g'),('d','h'),
                            ('d','j'),('e','k'),('e','l'),('f','m'),('g','o'),('h','i'),('m','n'),('o','p'),])

        #General cases (Random nodes for testing)                           #       Graphic of the binary tree
        self.assertEqual(lowest_common_ancestor(G, 'p', 'i'), 'a')          #                  _a_
        self.assertEqual(lowest_common_ancestor(G, 'n', 'o'), 'c')          #                /    \__
        self.assertEqual(lowest_common_ancestor(G, 'b', 'c'), 'a')          #                b       c__
        self.assertEqual(lowest_common_ancestor(G, 'h', 'c'), 'a')          #              /  \      /  \
        self.assertEqual(lowest_common_ancestor(G, 'i', 'l'), 'b')          #             d   e     f    g
        self.assertEqual(lowest_common_ancestor(G, 'i', 'j'), 'd')          #           / \  /\    /     \
                                                                            #          h  j k  l  m       o
                                                                            #         /          /         \
    def test_special_lca(self):                                             #        i          n           p
        #Creating graph with networkx library..
        G = nx.DiGraph()
        #Adding random nodes..
        G.add_nodes_from(['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p'])
        #Adding random edges..
        G.add_edges_from([('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('c','g'),('d','h'),
                            ('d','j'),('e','k'),('e','l'),('f','m'),('g','o'),('h','i'),('m','n'),('o','p'),])

        #Special cases (if one of the nodes is root, the LCA is the root)
        self.assertEqual(lowest_common_ancestor(G, 'a', 'b'), 'a')
        #LCA of nodes x and x is x
        self.assertEqual(lowest_common_ancestor(G, 'a', 'a'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'd', 'd'), 'd')


    def test_empty_graph(self):
        #Creating empty graph with networkx library..
        G = nx.DiGraph()
        self.assertEqual(lowest_common_ancestor(G, 'x', 'x'), None)



if __name__ == '__main__':
    unittest.main()
