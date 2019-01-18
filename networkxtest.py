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

	
	def test_is_weighted_without_weights(self):
		'''Test Case No 1a: Is Weighted with no weight'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1,2),(1,3),(1,4)])
		output=nx.is_weighted(graph)
		self.assertFalse(output)


	def test_is_weighted_positive_weights(self):
		'''Test Case No 1b: Is Weighted with positive weight'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1, 2, {'weight' : 2}), (1, 3, {'weight' : 4}), (1, 4, {'weight' : 6})])
		output=nx.is_weighted(graph)
		self.assertTrue(output)


	def test_is_weighted_negative_weights(self):
		'''Test Case No 1c: Is Weighted with negative weight'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1, 2, {'weight' : -2}), (1, 3, {'weight' : -4}), (1, 4, {'weight' : -6})])
		output=nx.is_weighted(graph)
		self.assertTrue(output)


	def test_is_negatively_weighted_without_weights(self):
		'''Test Case No 2a: Is Negatively Weighted with no weight'''
		graph=nx.Graph()
		graph.add_nodes_from([5,6,7,8])
		graph.add_edges_from([(5,6),(6,7),(7,8)])
		output=nx.is_negatively_weighted(graph)
		self.assertFalse(output)


	def test_is_negatively_weighted_negative_weights(self):
		'''Test Case No 2b: Is Negatively Weighted with negative weight'''
		graph=nx.Graph()
		graph.add_nodes_from([5,6,7,8])
		graph.add_edges_from([(5, 6, {'weight' : -1}), (6, 7, {'weight' : -2}), (7, 8, {'weight' : -3})])
		output=nx.is_negatively_weighted(graph)
		self.assertTrue(output)


	def test_is_negatively_weighted_positive_weights(self):
		'''Test Case No 2c: Is Negatively Weighted with positive weight'''
		graph=nx.Graph()
		graph.add_nodes_from([5,6,7,8])
		graph.add_edges_from([(5, 6, {'weight' : 1}), (6, 7, {'weight' : 2}), (7, 8, {'weight' : 3})])
		output=nx.is_negatively_weighted(graph)
		self.assertFalse(output)


	def test_set_node_attributes_true_value(self):
		'''Test Case No 3a: Set Node Attributes with True Value'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1,2),(1,3),(1,4)])

		nx.set_node_attributes(graph, {1:2}, name='value')
		output = graph.node[1]['value']
		result = 2
		self.assertEqual(output, result)


	def test_set_node_attributes_false_value(self):
		'''Test Case No 3b: Set Node Attributes with False Value'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1,2),(1,3),(1,4)])

		nx.set_node_attributes(graph, {1:2}, name='value')
		output = graph.node[1]['value']
		result = 4
		self.assertNotEqual(output, result)


	def test_set_node_attributes_string(self):
		'''Test Case No 3c: Set Node Attributes with string'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4])
		graph.add_edges_from([(1,2),(1,3),(1,4)])

		nx.set_node_attributes(graph, {1:'agnes'}, name='name')
		self.assertTrue((graph.node[1]['name'] == 'agnes'))


	def test_get_node_attributes_color(self):
		'''Test Case No 4a: Get Attributes with color'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4], color='blue')
		color = nx.get_node_attributes(graph, 'color')
		output = color[1]
		result = 'blue'
		self.assertEqual(output, result)
		

	def test_get_node_attributes_weight(self):
		'''Test Case No 4b: Get Attributes with weight'''
		graph=nx.Graph()
		graph.add_nodes_from([1,2,3,4], weight=2)
		weight = nx.get_node_attributes(graph, 'weight')
		output = weight[4]
		self.assertTrue((output == 2))


	def test_get_node_attributes_element(self):
		'''Test Case No 4c: Get Attributes, get one element'''
		graph = nx.Graph()
		graph.add_node('agnes', year=1996, country='sweden', occ='student')
		year = nx.get_node_attributes(graph, 'year')
		output = year['agnes']
		self.assertTrue((output == 1996))





if __name__ == '__main__':
    unittest.main()