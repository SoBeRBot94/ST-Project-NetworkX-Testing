#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''


import unittest
import networkx as nx

class NodesTest(unittest.TestCase):
    def test_integer_nodes(self):
        '''Should return the copy of the Graph's nodes in a list'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        nodeList = list(nx.nodes(graph))
        result = [1,2,3,4,5,6,7]
        self.assertListEqual(nodeList, result)

    def test_character_nodes(self):
        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        nodeList = sorted(list(nx.nodes(graph)))
        result = ['A','B','C','D','E']
        self.assertListEqual(nodeList, result)
    
    def test_number_of_nodes(self):
        '''Should return the number of nodes in the initialized graph'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        nodeLength = nx.number_of_nodes(graph)
        result = 7
        self.assertEqual(nodeLength, result)

if __name__ == '__main__':
    unittest.main()
