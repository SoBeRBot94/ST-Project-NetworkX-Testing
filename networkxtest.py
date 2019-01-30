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
        graph = nx.Graph([(1,2), (1,3), (1,4)])
        frozenGraph = nx.freeze(graph)
        try:
            frozenGraph.add_edges_from([(2,5),(3,6)])
        except nx.NetworkXError:
            output = list(nx.edges(frozenGraph))
            resList = [(1,2), (1,3), (1,4)]
            self.assertListEqual(output, resList)

        graph = nx.Graph([('a','b'), ('a','c'), ('a','d')])
        frozenGraph = nx.freeze(graph)
        try:
            frozenGraph.add_edges_from([('e','f'), ('g','h')])
        except nx.NetworkXError:
            output = sorted(list(nx.edges(frozenGraph)))
            resList = [('a','b'), ('a','c'), ('a','d')]
            self.assertListEqual(output, resList)

        graph = nx.Graph([('-1','-2'), ('-1','-3'), ('-1','-4')])
        frozenGraph = nx.freeze(graph)
        try:
            frozenGraph.add_edges_from([('-2','-5'), ('-3','-6')])
        except nx.NetworkXError:
            output = sorted(list(nx.edges(frozenGraph)))
            resList = [('-1','-2'), ('-1','-3'), ('-4','-1')]
            self.assertListEqual(output, resList)

if __name__ == '__main__':
    unittest.main()
