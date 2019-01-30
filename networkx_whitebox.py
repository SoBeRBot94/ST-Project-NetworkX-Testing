#!/usr/bin/env/python2.7
# -*- coding: utf-8 -*-
'''  
Softwaretesting project: Networkx 1.11

Team Number: 2
Student Names: Sudarsan Bhargavan, Valeria Helle, Agnes Lind, Anna Westergren
'''
  
  
import unittest
import networkx as nx
from coverage import Coverage as cov

cov.start()

  
  
  
cov.stop()
cov.save()

cov.html_report()

  
if __name__ == '__main__':
    unittest.main()