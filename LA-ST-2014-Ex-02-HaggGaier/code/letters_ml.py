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




  
i=0
mins = 0.1


#Run Classifier with increasing numbers of samples until it takes mins minutes
while True:
    i+=1
    samples = i*100
    s_2_1 = ScalabilityQuestion()
    start_time = time.time()
    training_X = s_2_1.data[0:samples][:,0:15]
    training_Y = s_2_1.encoded_letters[0:samples][:]
    
    s_2_1.build_classifier(training_X, training_Y)
    classifier_time = (time.time() - start_time)      
    
    threshold = s_2_1.clf.tree_.threshold
    
    test_X = s_2_1.data[samples:][:,0:15]
    test_Y = s_2_1.encoded_letters[samples:][:]
    
    #don't include visualization in classifier performance
    #s_2_1.draw_graph(s_2_1.clf, '8_'+str(samples)) 

    #with open('./timefile', 'a') as f:
        #f.write(str(i*100) + ' samples in ' + str(time.time() - start_time) + ' seconds\n')
        #f.write(str(samples) + ',' + str(classifier_time) + '\n')
        
    with open('./treesize_file', 'a') as f:
        f.write(str(samples) + ',' + str(len(threshold)) + '\n')
    
    count = 0
    letter_perf = np.zeros((26,2)) 
    for letter in range(len(test_X)):
        prediction = s_2_1.clf.predict(test_X[letter])
        actual = test_Y[letter]
        if actual == prediction:
            letter_perf[actual,0] += 1
        else:
            letter_perf[actual,1] += 1
        count +=1
        
        
    lfname = ('./letterdata' + str(samples))
    #with open(lfname, 'w') as lf:
        #lf.write(str(letter_perf))
        #lf.close()
    
    #s_2_1.draw_graph(s_2_1.clf, lfname)
    
    if classifier_time > 60*mins:
        break    
    print count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    