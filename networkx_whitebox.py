#!/usr/bin/env/python2.7
# -*- coding: utf-8 -*-
'''  
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''
  
  
import unittest
import networkx as nx

class AddEdges(unittest.TestCase):
    def test_add_edges_from_single_edge_with_key_new_vertex(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(5,6)], key=3)
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(5,6)]
        self.assertEqual(set(expOutput), set(result))

    def test_add_edges_from_single_edge_with_key_new_node(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(9,5)], key=4)
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(5,9)]
        self.assertEqual(set(expOutput), set(result))

    def test_add_edges_from_single_edge_with_key_new_node_new_vertex(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(6,7)], key=5)
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(6,7)]
        self.assertEqual(set(expOutput), set(result))
  
    def test_add_edges_from_single_edge_with_key_no_new_edge(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(1,3)], key='g')
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5)]
        self.assertListEqual(expOutput, result)
  
    def test_add_edges_from_single_edge_without_key_new_vertex(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(5,6)])
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(5,6)]
        self.assertEqual(set(expOutput), set(result))

    def test_add_edges_from_single_edge_without_key_new_node(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(9,5)])
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(5,9)]
        self.assertEqual(set(expOutput), set(result))

    def test_add_edges_from_single_edge_without_key_new_node_new_vertex(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(6,7)])
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(6,7)]
        self.assertEqual(set(expOutput), set(result))
  
    def test_add_edges_from_single_edge_without_key_no_new_edge(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(1,3)])
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5)]
        self.assertListEqual(expOutput, result)
  
    def test_add_edges_from_multi_valued_tuple(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        flag = False
        try:
            graph.add_edges_from([(7,8,9,0)])
            if len(nx.edges(graph)) > 5:
                flag = True
        except nx.NetworkXError:
            expOutput = list(nx.edges(graph))
            result = [(1,2),(1,3),(2,4),(3,4),(4,5)]
            if set(expOutput) == set(result):
                self.assertFalse(flag)

    def test_add_edges_from_multiple_tuples(self):
        graph = nx.Graph([(1,2),(1,3),(2,4),(3,4),(4,5)])
        graph.add_edges_from([(5,6),(1,3)], key='g')
        expOutput = list(nx.edges(graph))
        result = [(1,2),(1,3),(2,4),(3,4),(4,5),(5,6)]
        self.assertListEqual(expOutput, result)

if __name__ == '__main__':
    unittest.main()
