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
        '''Should return the copy of the Graph's nodes in a list - Integer'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        nodeList = list(nx.nodes(graph))
        result = [1,2,3,4,5,6,7]
        self.assertListEqual(nodeList, result)
        
        graph = nx.Graph([(-1,-2),(-1,-4),(-1,-5),(-2,-3),(-3,-4),(-3,-5),(-5,-6),(-6,-7)])
        nodeList = sorted(list(nx.nodes(graph)))
        result = [-7,-6,-5,-4,-3,-2,-1]
        self.assertListEqual(nodeList, result)

    def test_character_nodes(self):
        '''Should return the copy of the Graph's nodes in a list - Character'''
        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        nodeList = sorted(list(nx.nodes(graph)))
        result = ['A','B','C','D','E']
        self.assertListEqual(nodeList, result)
    
    def test_empty_nodes(self):
        '''Should return the copy of the Graph's nodes in a list - Empty'''
        graph = nx.Graph()
        result = []
        self.assertListEqual(result, list(nx.nodes(graph)))

    def test_number_of_nodes_non_empty(self):
        '''Should return the number of nodes in the initialized graph - NonEmpty'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        nodeLength = nx.number_of_nodes(graph)
        result = 7
        self.assertEqual(nodeLength, result)
        
        graph = nx.Graph([(-1,-2),(-1,-4),(-1,-5),(-2,-3),(-3,-4),(-3,-5),(-5,-6),(-6,-7)])
        nodeLength = nx.number_of_nodes(graph)
        result = 7
        self.assertEqual(nodeLength, result)
        
        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        nodeLength = nx.number_of_nodes(graph)
        result = 5
        self.assertEqual(nodeLength, result)

    def test_number_of_nodes_empty(self):
        '''Should return the number of nodes in the initialized graph - Empty'''
        graph = nx.Graph()
        nodeLength = nx.number_of_nodes(graph)
        self.assertEqual(nodeLength, 0)

    def test_connected_neighbors_non_empty(self):
        '''Should return a list with all the connected neighboring nodes of a node N - NonEmpty'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        nodeNeighbors = list(nx.neighbors(graph, 1))
        result = [2,4,5]
        self.assertListEqual(nodeNeighbors, result)

        graph = nx.Graph([(-1,-2),(-1,-4),(-1,-5),(-2,-3),(-3,-4),(-3,-5),(-5,-6),(-6,-7)])
        nodeNeighbors = sorted(list(nx.neighbors(graph, -3)))
        result = [-5,-4,-2]
        self.assertListEqual(nodeNeighbors, result)

        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        nodeNeighbors = list(nx.neighbors(graph,'E'))
        result = ['D']
        self.assertListEqual(nodeNeighbors, result)

    def test_connected_neighbors_empty(self):
        '''Should reutn a list with all the connected neighboring nodes of a node N - Empty'''
        graph = nx.Graph()
        flag = False
        try:
            nodeNeighbors = nx.neighbors(graph, 1)
            flag = True
        except nx.NetworkXError:
            self.assertFalse(flag)

    def test_all_neighbors_non_empty(self):
        '''Should return a list with all the neighboring nodes of a node N - NonEmpty'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        allNodeNeighbors = list(nx.all_neighbors(graph, 5))
        result = [1,3,6]
        self.assertListEqual(allNodeNeighbors, result)

        graph = nx.Graph([(-1,-2),(-1,-4),(-1,-5),(-2,-3),(-3,-4),(-3,-5),(-5,-6),(-6,-7)])
        allNodeNeighbors = sorted(list(nx.all_neighbors(graph, -1)))
        result = [-5,-4,-2]
        self.assertListEqual(allNodeNeighbors, result)

        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        allNodeNeighbors = sorted(list(nx.all_neighbors(graph, 'B')))
        result = ['A','C']
        self.assertListEqual(allNodeNeighbors, result)

    def test_all_neighbors_empty(self):
        '''Should return a list with all the neighboring nodes of a node N - Empty'''
        graph = nx.Graph()
        flag = False
        try:
            allNodeNeighbors = nx.all_neighbors(graph, 2)
            flag = True
        except nx.NetworkXError:
            self.assertFalse(flag)

    def test_non_neighbors_non_empty(self):
        '''Should return a list with all the non neighboring nodes of a node N - NonEmpty'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        nonNodeNeighbors = list(nx.non_neighbors(graph, 4))
        result = [2,5,6,7]
        self.assertListEqual(nonNodeNeighbors, result)

        graph = nx.Graph([(-1,-2),(-1,-4),(-1,-5),(-2,-3),(-3,-4),(-3,-5),(-5,-6),(-6,-7)])
        nonNodeNeighbors = sorted(list(nx.non_neighbors(graph, -1)))
        result = [-7,-6,-3]
        self.assertListEqual(nonNodeNeighbors, result)

        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        nonNodeNeighbors = sorted(list(nx.non_neighbors(graph, 'B')))
        result = ['D','E']
        self.assertListEqual(nonNodeNeighbors, result)

    def test_non_neigbors_empty(self):
        '''Should return a list with all the non neighboring nodes of a node N - Empty'''
        graph = nx.Graph()
        flag = False
        try:
            nonNodeNeighbors = nx.non_neighbors(graph, 2)
            flag = True
        except nx.NetworkXError:
            self.assertFalse(flag)

    def test_common_neighbors_non_empty(self):
        '''Should return a list with all the neighboring nodes that are common between nodes N & M - NonEmpty'''
        graph = nx.Graph([(1,2),(1,4),(1,5),(2,3),(3,4),(3,5),(5,6),(6,7)])
        commonNodeNeighbors = list(nx.common_neighbors(graph, 4, 5))
        result = [1,3]
        self.assertListEqual(commonNodeNeighbors, result)

        graph = nx.Graph([(-1,-2),(-1,-4),(-1,-5),(-2,-3),(-3,-4),(-3,-5),(-5,-6),(-6,-7)])
        commonNodeNeighbors = sorted(list(nx.common_neighbors(graph, -2, -4)))
        result = [-3,-1]
        self.assertListEqual(commonNodeNeighbors, result)

        graph = nx.Graph([('A','B'),('A','C'),('B','C'),('C','D'),('D','E')])
        commonNodeNeighbors = sorted(list(nx.common_neighbors(graph, 'A', 'D')))
        result = ['C']
        self.assertListEqual(commonNodeNeighbors, result)

    def test_common_neigbors_empty(self):
        '''Should return a list with all the neighboring nodes that are common between nodes N & M - Empty'''
        graph = nx.Graph()
        flag = False
        try:
            commonNodeNeighbors = nx.common_neighbors(graph, 2, 3)
            flag = True
        except nx.NetworkXError:
            self.assertFalse(flag)

if __name__ == '__main__':
    unittest.main()
