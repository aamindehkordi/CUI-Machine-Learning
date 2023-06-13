import pandas as pd
import numpy as np
import argparse
from sklearn.ensemble import RandomForestClassifier
import os
from sklearn.metrics import accuracy_score

#parser = argparse.ArgumentParser(description='Titanic passenger survival prediction using Random Forest Classifier')
#parser.add_argument('filename', type=str, help='name of a valid csv file')
#args = parser.parse_args()
#if not os.path.exists(args.filename) or not os.path.isfile(args.filename):
#    print('Error: "{}" is not a valid file'.format(args.filename))
#    exit()
     
td = pd.read_csv("titanic_dataset.csv")
test = pd.read_csv("titanic_predictions.csv")

trainingdata = td
testdata = test

data = pd.concat((trainingdata.loc[:,'Sex':'Fare'],
                      testdata.loc[:,'Sex':'Fare']))
data = pd.get_dummies(data)
data = data.fillna(data.mean())
data.isna().sum()

xTrain = data[:trainingdata.shape[0]]
xtest = data[trainingdata.shape[0]:]
y = td["Survived"]
category = ["Pclass", "Sex", "SibSp", "Parch"]
x = pd.get_dummies(td[category])
xtest = pd.get_dummies(test[category])
rfc = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
rfc.fit(xTrain, y)
predictions = rfc.predict(xtest)

results = pd.DataFrame({'PassengerId': testdata.PassengerId, 'Survived': predictions})
print(results)
print(f"Accuracy: {accuracy_score(xtest,predictions)*100}%")


#output.to_csv('titanicresults.csv', index=False)
    