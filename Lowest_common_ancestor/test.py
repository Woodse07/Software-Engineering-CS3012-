import unittest
import networkx as nx
from LCA import lowest_common_ancestor

class myTest(unittest.TestCase):
    def test_correct_lca(self):
        G = nx.DiGraph()
        G.add_nodes_from(['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p'])
        G.add_edges_from([('a','b'),('a','c'),('b','d'),('b','e'),('c','f'),('c','g'),('d','h'),
                            ('d','j'),('e','k'),('e','l'),('f','m'),('g','o'),('h','i'),('m','n'),('o','p'),])

        self.assertEqual(lowest_common_ancestor(G, 'p', 'i'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'n', 'o'), 'c')
        self.assertEqual(lowest_common_ancestor(G, 'b', 'c'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'h', 'c'), 'a')
        self.assertEqual(lowest_common_ancestor(G, 'i', 'l'), 'b')
        self.assertEqual(lowest_common_ancestor(G, 'i', 'j'), 'd')
        #self.assertEqual(lowest_common_ancestor(G, 'a', 'b'), 'a')
        #self.assertEqual(lowest_common_ancestor(G, 'a', 'a'), 'a')

if __name__ == '__main__':
    unittest.main()
