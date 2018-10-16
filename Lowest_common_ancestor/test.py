import unittest
import networkx as nx
from LCA_dag import lowest_common_ancestor
from binary_tree import Node

class myTest(unittest.TestCase):
    def test_general_lca(self):
        #Creating graph with networkx library..
        G = nx.DiGraph()
        #Adding random nodes..
        G.add_nodes_from(['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p'])
        #Adding random edges..
        G.add_edges_from([('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('c','g'),('d','h'),
                            ('d','j'),('e','k'),('e','l'),('f','m'),('g','o'),('h','i'),('m','n'),('o','p'),])

        #General cases (Random nodes for testing)                           #       Graphic of the is_directed_acyclic_graph
        self.assertEqual(lowest_common_ancestor(G, 'p', 'i'), 'a')          #                  _a_
        self.assertEqual(lowest_common_ancestor(G, 'n', 'o'), 'c')          #                /    \__
        self.assertEqual(lowest_common_ancestor(G, 'b', 'c'), 'a')          #                b       c__
        self.assertEqual(lowest_common_ancestor(G, 'h', 'c'), 'a')          #              /  \      /  \
        self.assertEqual(lowest_common_ancestor(G, 'i', 'l'), 'b')          #             d   e     f    g
        self.assertEqual(lowest_common_ancestor(G, 'i', 'j'), 'd')          #           / \  /\    /     \
        self.assertEqual(lowest_common_ancestor(G, 'i', 'd'), 'd')          #          h  j k  l  m       o
        self.assertEqual(lowest_common_ancestor(G, 'p', 'c'), 'c')          #         /          /         \
                                                                            #        i          n           p

    def test_special_lca(self):
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

    def test_singleton_graph(self):
        #Creating singleton graph with networkx library..
        G = nx.DiGraph()
        G.add_node('x')
        self.assertEqual(lowest_common_ancestor(G,'x','x'), None)

    def test_wrong_parameters(self):
        G = "Hello World"
        self.assertEqual(lowest_common_ancestor(G, 'x', 'x'), None)

        G = 7
        self.assertEqual(lowest_common_ancestor(G, 'x', 'x'), None)

        G = [1, 2, 3]
        self.assertEqual(lowest_common_ancestor(G, 'x', 'x'), None)

        G = 5.4
        self.assertEqual(lowest_common_ancestor(G, 'x', 'x'), None)

    def test_node_exists(self):
        #Creating graph with networkx library..
        G = nx.DiGraph()
        #Adding random nodes..
        G.add_nodes_from(['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p'])
        #Adding random edges..
        G.add_edges_from([('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('c','g'),('d','h'),
                            ('d','j'),('e','k'),('e','l'),('f','m'),('g','o'),('h','i'),('m','n'),('o','p'),])

        self.assertEqual(lowest_common_ancestor(G, 1, 2), None)
        self.assertEqual(lowest_common_ancestor(G, 'x', 'z'), None)
        self.assertEqual(lowest_common_ancestor(G, 'w', 'y'), None)

    def test_directed_acyclic(self):                                                            #           _a_
        #Creating graph with networkx library..                                                 #         /    \
        G = nx.DiGraph()                                                                        #        b      c
        #Adding random nodes                                                                    #        |      |
        G.add_nodes_from(['a','b','c','d','e','f'])                                             #        d      e
        #Adding random edges                                                                    #         \    /
        G.add_edges_from([('a','b'),('a','c'),('b','d'),('c','e'),('d','f'),('e','f')])         #           f

        #Testing acyclic
        self.assertTrue(nx.is_directed_acyclic_graph)
        self.assertEqual(lowest_common_ancestor(G, 'f', 'b'), 'b')
        self.assertEqual(lowest_common_ancestor(G, 'd', 'e'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'a', 'a'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'd', 'c'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'f', 'f'), 'f')

    def test_binary_tree(self):
        BT = Node(10)
        BT.insert(5)
        BT.insert(15)
        self.assertEqual(BT.data, 10)
        self.assertEqual(BT.left.data, 5)
        self.assertEqual(BT.right.data, 15)

        BT.insert(25)
        BT.insert(2)
        self.assertEqual(BT.left.left.data, 2)
        self.assertEqual(BT.right.right.data, 25)

if __name__ == '__main__':
    unittest.main()
