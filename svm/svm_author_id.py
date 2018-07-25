#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn import svm, metrics

t0 = time()
clf = svm.SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
labels_pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

print(metrics.accuracy_score(labels_test, labels_pred))

count_chris = 0
for label in labels_pred:
	if label == 1:
		count_chris += 1
print 'no. of emails from Chris: ', count_chris
#########################################################


