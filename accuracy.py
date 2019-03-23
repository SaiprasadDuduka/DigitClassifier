import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('D:\\My Projects\\Digit Classifier - ML\\csv\\dataset.csv').values
clf = DecisionTreeClassifier()
size = 200
#training dataset
xtrain = data[0:size, 1:]
train_label = data[0:size, 0]

clf.fit(xtrain, train_label)

#testing data
xtest = data[size:, 1:]
actual_label = data[size:, 0]

p = clf.predict(xtest)

count = 0
for i in range(len(actual_label)):
	count += 1 if p[i] == actual_label[i] else 0
	
print("Accuracy : ", round((count/len(actual_label)) * 100, 2), '%')
tp = input()