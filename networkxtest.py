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
        #nodeList = list(nx.nodes(graph))
        nodeList = list(nx.nodes(graph))
        result = [1,2,3,4,5,6,7]
        #self.assertListEqual(nodeList, result)
        self.assertEqual(set(nodeList),set(result))
        
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
class GraphTest(unittest.TestCase):
    def test_even_degree(self):
        #allows us to test a handshake lemma:
        #every finite undirected graph has an even number of vertices with odd degree
        #(the number of edges touching the vertex). In more colloquial terms, in a party of people some of whom shake hands,
        #an even number of people must have shaken an odd number of other people's hands. 
        testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        degree = nx.degree(testgraph)
        result = 0
        for el in degree:
            if(el[1] % 2!=0):
                result = result + 1
        self.assertTrue(result % 2 == 0)
        testgraph.add_edge(6,7)
        degree = nx.degree(testgraph)
        result = 0
        for el in degree:
            if(el[1] % 2!=0):
                result = result + 1
        self.assertFalse(result % 2 != 0)
    def test_degree(self):
        #test whether function degree works as it should basic case
        testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        degree = nx.degree(testgraph, 5)
        self.assertEqual(degree, 3)
        #test whether function degree works as it should after node removal
        testgraph.remove_edge(1,5)
        degree = nx.degree(testgraph, 5)
        self.assertEqual(degree, 2)
        #test whether degree of every node in a graph is at least one
        list_degree = []
        list_nodes = nx.nodes(testgraph)
        for el in list_nodes:
            degree = nx.degree(testgraph, el)
            list_degree.append(degree)
        for en in list_degree:
            self.assertTrue(en>=1)
    def test_is_directed(self):
        #test whether directed graph is identified as directed 
        testgraph = nx.DiGraph([(1,2),(1,4),(2,4),(4,3),(3,1),(3,2)])
        self.assertTrue(nx.is_directed(testgraph))
        #test whether nondirected graph is falsly  identified as directed 
        testgraph = nx.Graph([(1,2),(1,4),(2,4),(4,3),(3,1),(3,2)])
        self.assertFalse(nx.is_directed(testgraph))
    def test_density(self):
        #test that density calculated by the function nx.density equals to 
        #density calculated with the density formula for undirected graph
        testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        edges = len(nx.edges(testgraph))
        nodes = len(nx.nodes(testgraph))
        density = (2 * edges)/(nodes* (nodes-1))
        self.assertEqual(density, nx.density(testgraph))
        #test that density calculated by the function nx.density equals to 
        #density calculated with the density formula for directed graph
        testgraph_di = nx.DiGraph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        edges_di = len(nx.edges(testgraph_di))
        nodes_di = len(nx.nodes(testgraph_di))
        density_di = (edges_di)/(nodes_di* (nodes_di-1))
        self.assertEqual(density_di, nx.density(testgraph_di))
        self.assertFalse(nx.density(testgraph_di) == nx.density(testgraph))
        #test that density of an empty grpah equals to 0
        testgraph = nx.Graph([])
        self.assertEqual(nx.density(testgraph),0)
        #test that density of a complete grpah equals to 1
        testgraph =  nx.Graph([(1,2),(2,3),(3,1)])
        self.assertEqual(nx.density(testgraph),1)
    def test_create_empty_copy(self):
        #tests that graph copy has no edges
        testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        copy_graph = nx.create_empty_copy(testgraph)
        edges = len(nx.edges(copy_graph))
        self.assertEqual(edges,0)
        #tests that graph copy still has nodes
        nodes = len(nx.nodes(copy_graph))
        self.assertEqual(nodes,len(testgraph))
        #tests that graph copy still has no edges and therefore a degree for any node should be 0
        degree = nx.degree(copy_graph, 5)
        self.assertEqual(degree,0)
        #tests that graph copy has no edges and therefore density should be 0
        self.assertEqual(0, nx.density(copy_graph))
        #tests that graph copy only gets edges if added manually
        copy_graph.add_edge(1,2)
        degree = nx.degree(copy_graph, 1)
        self.assertEqual(degree,1)
        
class EdgesTest(unittest.TestCase):
    def test_edges(self):
        #tests whether number of edges for a certain node is calculated correctly 
        testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        graph_edges = nx.edges(testgraph,1)
        self.assertEqual(len(graph_edges),2)
        #tests whether number of edges for a certain node is calculated correctly after removal
        testgraph.remove_edge(1,5)
        print(testgraph)
        graph_edges = nx.edges(testgraph,1)
        self.assertEqual(len(graph_edges), 1)
        graph_edges = nx.edges(testgraph)
        self.assertEqual(len(graph_edges), len(testgraph))
    def test_non_edges(self):
        testgraph = nx.Graph([(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)])
        non_edges = nx.non_edges(testgraph)
        self.assertTrue((1,3) in non_edges)
        self.assertFalse((1,2) in non_edges)
        testgraph.add_edge(1,3)
        non_edges = nx.non_edges(testgraph)
        self.assertFalse((1,3) in non_edges)

    def test_number_of_edges(self):
        testgraph = nx.Graph([])
        number_of_edges = nx.number_of_edges(testgraph)
        self.assertEqual(number_of_edges,0)
        testgraph.add_edge(1,2)
        testgraph.add_edge(2,3)
        number_of_edges = nx.number_of_edges(testgraph)
        self.assertEqual(number_of_edges,len(testgraph)-1)

if __name__ == '__main__':
    unittest.main()
