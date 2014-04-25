#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 00:32:05 2014

@author: alex
"""

import numpy as np
import sklearn
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot
import time

class ScalabilityQuestion(object):
    def __init__(self):
        self.prepare_data()
        
    def prepare_data(self):
        # Read the data from file
        data = np.genfromtxt('data/letter-recognition/letter-recognition.data',
                             delimiter=',')
        self.data = np.delete(data, 0, 1)
        # The first column of data is of type string, amd wasn't read properly
        data_raw = np.genfromtxt('data/letter-recognition/letter-recognition.data',
                                 delimiter=',', dtype=None)
#        data_raw = np.genfromtxt('data/letter-recognition/letter_test.data',
#                         delimiter=',', dtype=None)
        letters = list()
        for i in xrange(data_raw.size):
            letters.append(data_raw[i][0])        
        letters = np.array(letters)
        # Now encode the strings 
        self.le = sklearn.preprocessing.LabelEncoder()
        self.le.fit(letters)
        self.encoded_letters = self.le.transform(letters)[:,np.newaxis]

    def build_classifier(self, data, labels, criterion='gini'):
        clf = tree.DecisionTreeClassifier(criterion)
        self.clf = clf.fit(data, labels)
        
    def draw_graph(self, classifier, filename="out"):
        dot_data = StringIO()    
        tree.export_graphviz(classifier, out_file=dot_data)
        graph = pydot.graph_from_dot_data(dot_data.getvalue())
        graph.write_svg(filename+".svg")        


s_2_1 = ScalabilityQuestion()

    # Sort and split data in 'letter' groups
    # For a group: get the mean
    
    # Noise is now defined by the distance (euclidean parameter distance) 
    # between a letter and its category mean
    
    # up to distance_C (=..) we call this innerclass noise
    # over distance_O we call this interclass noise
    
    # The number of noisy instances / number of nonnoisy instances * 100% 
    
    # In order to control the noise, we need to select smaller training/test 
    # set from the original set in such a way, that we can approximate n% noise