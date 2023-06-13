import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import csv

if __name__ == '__main__':
    df = pd.read_csv("train.csv")
    td = pd.read_csv("test.csv")

    xLabels = ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Cabin"]

    #Removes empty datapoints from data
    df = df.fillna(df.mean())
    td = td.fillna(td.mean())
    df.isna().sum()
    td.isna().sum()
    df = df.dropna(how='any')
    td = td.dropna(how='any')


    y = df["Survived"]
    X = df[xLabels]
    tX = td[xLabels]

    #Convert Categorical Data into Numerical Data

    X["Sex"] = X["Sex"].map({'male': 1, 'female': 0})
    for i, row in X['Cabin'].iteritems():
        X['Cabin'] = X['Cabin'].replace(row, row[0])

    tX["Sex"] = tX["Sex"].map({'male': 1, 'female': 0})
    for i, row in tX['Cabin'].iteritems():
        tX['Cabin'] = tX['Cabin'].replace(row, row[0])

    X['Cabin'] = X['Cabin'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'T': 7})
    tX['Cabin'] = tX['Cabin'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'T': 7})



    rFC = RandomForestClassifier(n_estimators=1000, max_depth=5, random_state=3)
    rFC.fit(X, y)
    preds = rFC.predict(tX)
    results = pd.DataFrame(data={'PassengerId': td.PassengerId, 'Survived': preds})
    print(results)

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for index, row in enumerate(preds):
            if index == 0:
                writer.writerow(['PassengerId', 'Survived'])
                writer.writerow([tX.iloc[index, 0], preds[index]])
            else:
                writer.writerow([tX.iloc[index, 0], preds[index]])