import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

mushroomdata = pd.read_csv('mushrooms_saved.csv')

def encoded(features):
    encoder=LabelEncoder()
    encoder.fit(features)
    print(features.name,encoder.classes_)
    return encoder.transform(features)

for col in mushroomdata.columns:
    mushroomdata[str(col)] = encoded(mushroomdata[str(col)])
    
y = mushroomdata['class']
x = mushroomdata.drop('class',axis=1)

xtrain,xtest,ytrain,ytest = train_test_split (x,y,test_size=0.2)

rfc = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1) 
rfc.fit(xtrain,ytrain)
pred = rfc.predict(xtest)

print(f"Accuracy: {accuracy_score(ytest,pred)*100}%")
