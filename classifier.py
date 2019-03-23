import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import csv

def predict():
	#Training data
	train_data = pd.read_csv('D:\\My Projects\\Digit Classifier - ML\\csv\\dataset.csv').values
	clf = DecisionTreeClassifier()
	
	#Testing data
	test_data = pd.read_csv('D:\\My Projects\\Digit Classifier - ML\\csv\\pixel_num.csv').values

	#Training model
	clf.fit(train_data[0:,1:], train_data[0:,0])
	
	#Predicting answer
	ans = clf.predict(test_data)
	#print(ans[0])
	
	#Store the predicted number in ans.csv
	with open('D:\\My Projects\\Digit Classifier - ML\\csv\\ans.csv', 'w', newline = '') as f:
		thewriter = csv.writer(f)
		thewriter.writerow([ans[0]])
		thewriter.writerow([ans[0]])