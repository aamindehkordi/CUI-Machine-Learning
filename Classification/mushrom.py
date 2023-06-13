import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("mushrooms_saved.csv")

X_names = [*data.keys()]
y_names = X_names.pop(-1)

df = data[X_names]
for column in X_names:
    tempDF = pd.get_dummies(data[column], prefix=column)
    df = pd.merge(left=df,right=tempDF, left_index=True, right_index=True)

    df = df.drop(columns=column)
X_names = [*df.keys()]

x = df[X_names]
y = data[y_names].map({"'e'" : 1, "'p'" : 0})

xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=.189)

rFC = RandomForestClassifier(n_estimators=100,max_depth=5,random_state=1)
rFC.fit(xTrain, yTrain)
pred = rFC.predict(xTest)

print(f"Accuracy: {accuracy_score(yTest,pred)*100}%")

