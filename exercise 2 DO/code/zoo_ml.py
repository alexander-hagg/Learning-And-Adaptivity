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

    def build_classifier(self, data, labels, criterion='gini'):
        clf = tree.DecisionTreeClassifier(criterion)
        self.clf = clf.fit(data, labels)
    
    def draw_graph(self, classifier, filename="out"):
        dot_data = StringIO()    
        tree.export_graphviz(classifier, out_file=dot_data)
        graph = pydot.graph_from_dot_data(dot_data.getvalue())
        graph.write_svg(filename+".svg")

s_1_gini = SimplePredictionQuestion()
X = s_1_gini.data[:][:,0:15]
Y = s_1_gini.data[:][:,16]
s_1_gini.build_classifier(X, Y)
s_1_gini.draw_graph(s_1_gini.clf, '7-1-gini')

s_1_entropy = SimplePredictionQuestion()
X = s_1_entropy.data[:][:,0:15]
Y = s_1_entropy.data[:][:,16]
s_1_entropy.build_classifier(X, Y, 'entropy')
s_1_entropy.draw_graph(s_1_entropy.clf, '7-1-entropy')

#####

s_2_gini = SimplePredictionQuestion()
X = np.hstack((s_2_gini.encoded_zoo, s_2_gini.data[:][:,0:15]))
Y = s_2_gini.data[:][:,16]
s_2_gini.build_classifier(X, Y)
s_2_gini.draw_graph(s_2_gini.clf, '7-2-gini')

s_2_entropy = SimplePredictionQuestion()
X = np.hstack((s_2_gini.encoded_zoo, s_2_gini.data[:][:,0:15]))
Y = s_2_entropy.data[:][:,16]
s_2_entropy.build_classifier(X, Y, 'entropy')
s_2_entropy.draw_graph(s_2_entropy.clf, '7-2-entropy')

####

s_3_gini = SimplePredictionQuestion()
X = s_3_gini.data[:][:,[0,1,2,3,5,6,7,8,9,10,11,12,13,14,15]]
Y = s_3_gini.data[:][:,4]
s_3_gini.build_classifier(X, Y)
s_3_gini.draw_graph(s_3_gini.clf, '7-3-gini')

#s_3_gini.clf.predict([[0,0,1,0,1,1,1,1,0,0,1,0,1,0,1]])

####

s_4_gini = SimplePredictionQuestion()
X = s_4_gini.data[:][:,1:16]
Y = s_4_gini.encoded_zoo
s_4_gini.build_classifier(X, Y)
s_4_gini.draw_graph(s_4_gini.clf, '7-4-gini')
