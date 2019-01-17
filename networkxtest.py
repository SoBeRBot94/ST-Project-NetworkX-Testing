#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''


import unittest
import networkx as nx

class TestAttributes(unittest.TestCase):
	#Test Case No 1a
	def test_is_weighted(self):
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1,2),(1,3),(1,4)])
		output=nx.is_weighted(graph)
		self.assertFalse(output)

	#Test Case No 1b
		graph.add_edges_from([(1, 2, {'weight' : 2}), (1, 3, {'weight' : 4}), (1, 4, {'weight' : 6})])
		output=nx.is_weighted(graph)
		self.assertTrue(output)

	#Test Case No 1c
		graph.add_edges_from([(1, 2, {'weight' : -2}), (1, 3, {'weight' : -4}), (1, 4, {'weight' : -6})])
		output=nx.is_weighted(graph)
		self.assertTrue(output)


	#Test Case No 2a
	def test_is_negatively_weighted(self):
		graph=nx.Graph()
		graph.add_nodes_from([5,6,7,8])
		graph.add_edges_from([(5,6),(6,7),(7,8)])
		output=nx.is_negatively_weighted(graph)
		self.assertFalse(output)

	#Test Case No 2b
		graph.add_edges_from([(5, 6, {'weight' : -1}), (6, 7, {'weight' : -2}), (7, 8, {'weight' : -3})])
		output=nx.is_negatively_weighted(graph)
		self.assertTrue(output)

	#Test Case No 2c
		graph.add_edges_from([(5, 6, {'weight' : 1}), (6, 7, {'weight' : 2}), (7, 8, {'weight' : 3})])
		output=nx.is_negatively_weighted(graph)
		self.assertFalse(output)



if __name__ == '__main__':
    unittest.main()