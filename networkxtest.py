#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''


import unittest
import networkx as nx

class TestFreezingGraphStructure(unittest.TestCase):
    def test_freeze(self):
        '''Should return the same list of nodes after the graph is frozen'''
        graph = nx.Graph([(1,2), (1,3), (1,4)])
        frozenGraph = nx.freeze(graph)
        try:
            frozenGraph.add_edges_from([(2,5),(3,6)])
        except nx.NetworkXError:
            print("The Graph is Frozen !")
        Output = list(nx.edges(frozenGraph))
        Result = [(1,2), (1,3), (1,4)]
        self.assertListEqual(Output, Result)

if __name__ == '__main__':
    unittest.main()
