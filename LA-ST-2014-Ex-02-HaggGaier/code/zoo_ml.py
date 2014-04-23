#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Alexander Hagg and Adam Gaier
"""
import numpy as np
import sklearn
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

# hint: Python 1d arrays, vs row and column vectors
# A = np.arange(10)
# print A.shape
# print A[:, np.newaxis]
# print A[np.newaxis, :]

class SimplePredictionQuestion(object):
    def __init__(self):
        self.prepare_data()

    def prepare_data(self):
        # Read the data from file
        data = np.genfromtxt('data/zoo/zoo.data',
                             delimiter=',')
        self.data = np.delete(data, 0, 1)
        # The first column of data is of type string, amd wasn't read properly
        data_raw = np.genfromtxt('data/zoo/zoo.data',
                                 delimiter=',', dtype=None)
        zoo = list()
        for i in xrange(data_raw.size):
            zoo.append(data_raw[i][0])        
        zoo = np.array(zoo)
        # Now encode the strings 
        self.le = sklearn.preprocessing.LabelEncoder()
        self.le.fit(zoo)
        self.encoded_zoo = self.le.transform(zoo)[:,np.newaxis]
        self.zoo = zoo
        print "done preparing data"
        
    
    def draw_graph(self, classifier, filename="out.svg"):
        dot_data = StringIO()    
        tree.export_graphviz(classifier, out_file=dot_data)
        graph = pydot.graph_from_dot_data(dot_data.getvalue())
        graph.write_svg(filename+".svg")

s1 = SimplePredictionQuestion()
s1.draw_graph()