#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score

X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.30, random_state=42)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print clf.score(X_test, y_test)
print len([y for y in y_test if y == 1]) #No. of actual POI
print len(y_test) #No. of people in test dataset
true_values = [i for i, j in zip(pred, y_test) if i == j] 
print len([y for y in true_values if y == 1])#Find True positives
print precision_score(y_test, pred)
print recall_score(y_test, pred)



