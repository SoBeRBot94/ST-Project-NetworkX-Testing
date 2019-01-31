#!/usr/bin/env/python2.7
# -*- coding: utf-8 -*-
'''  
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''
  
  
import unittest
import networkx as nx

class RemoveEdges(unittest.TestCase):
	def test_remove_edges_from_base_case(self):
		'''adj = self.adj
        for e in ebunch:
            u, v = e[:2]  # ignore edge data if present
            if u in adj and v in adj[u]:
                del adj[u][v]
                if u != v:  # self loop needs only one entry removed
                    del adj[v][u]'''
		testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
		result = testgraph
		testgraph.remove_edges_from([(6,7)])
		self.assertEqual(result, testgraph)
	def test_remove_edges_from_one_edge(self):
		testgraph = nx.Graph([(1,1)])
		testgraph.remove_edges_from([(1,1,5)])
		result = testgraph.edges()
		self.assertTrue(len(result)==0)
	def test_remove_edges_from_multi_edge(self):
		testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
		nbunch = [(1,2), (2,5), (3,4)]
		testgraph.remove_edges_from(nbunch)
		result = nx.non_edges(testgraph)
		for el in nbunch:
		    self.assertTrue(el in result)
	def test_remove_all(self):
		G = nx.Graph()
		G.add_path([0,1,2,3])
		ebunch=[(0,1),(1,2),(2,3)]
		G.remove_edges_from(ebunch)
		result = G.edges()
		testgraph = nx.Graph()
		self.assertEqual(testgraph.edges(), result)

  
if __name__ == '__main__':
    unittest.main()
