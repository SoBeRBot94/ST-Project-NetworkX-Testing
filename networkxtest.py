#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''


import unittest
import networkx as nx


class GraphTest(unittest.TestCase):
	def test_even_density(self):
		'''allows us to test a handshake lemma:
		every finite undirected graph has an even number of vertices with odd degree
		 (the number of edges touching the vertex). In more colloquial terms, in a party of people some of whom shake hands,
		  an even number of people must have shaken an odd number of other people's hands. '''
		testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
		density = nx.degree(testgraph)
		result = 0
		for el in density:
			if(el[1] % 2!=0):
				result = result + 1
		self.assertTrue(result % 2 == 0)
		testgraph.add_edge(6,7)
		density = nx.degree(testgraph)
		result = 0
		for el in density:
			if(el[1] % 2!=0):
				result = result + 1
		self.assertFalse(result % 2 != 0)
	def test_degree(self):
		testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
		degree = nx.degree(testgraph, 5)
		self.assertEqual(degree, 3)
		testgraph.remove_edge(1,5)
		degree = nx.degree(testgraph, 5)
		self.assertEqual(degree, 2)
	def test_is_directed(self):
		testgraph = nx.DiGraph([(1,2),(1,4),(2,4),(4,3),(3,1),(3,2)])
		self.assertTrue(nx.is_directed(testgraph))

    	
class EdgesTest(unittest.TestCase):
	def test_edges(self):
		testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
		graph_edges = nx.edges(testgraph,1)
		self.assertEqual(len(graph_edges),2)
		testgraph.remove_edge(1,5)
		graph_edges = nx.edges(testgraph,1)
		self.assertEqual(len(graph_edges), 1)
	def test_non_edges(self):
		testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
		non_edges = nx.non_edges(testgraph)
		self.assertTrue((1,3) in non_edges)
		self.assertFalse((1,2) in non_edges)


    








if __name__ == '__main__':
    unittest.main()
    
    
    