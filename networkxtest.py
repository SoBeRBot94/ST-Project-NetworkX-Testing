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
	def test_is_weighted(self):
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1,2),(1,3),(1,4)])

		output=nx.is_weighted(graph)
		self.assertFalse(output)

		graph.add_edges_from([(1, 2, {'weight' : 2}), (1, 3, {'weight' : 4}), (1, 4, {'weight' : 6})])
		output=nx.is_weighted(graph)
		self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()