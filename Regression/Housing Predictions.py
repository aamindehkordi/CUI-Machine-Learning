import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dk = pd.read_csv("housing_test.csv")
df = pd.read_csv('housing_data.csv')
df = df.dropna()

encoder1 = OrdinalEncoder()
encoder2 = OrdinalEncoder()
encoder1.fit(df[['ocean_proximity']])
encoder2.fit(dk[['ocean_proximity']])
df['ocean_proximity'] = encoder1.transform(df[['ocean_proximity']])
dk['ocean_proximity'] = encoder2.transform(dk[['ocean_proximity']])
df['ocean_proximity'].value_counts()
dk['ocean_proximity'].value_counts()

y = df["median_house_value"]
X = df.drop('median_house_value', axis='columns')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.2)
model = LinearRegression()
model.fit(X, y)

y_pred = pd.DataFrame(model.predict(dk))
houseid = pd.DataFrame(dk['house_id'])
houseid = houseid.join(y_pred)
houseid.to_csv("housing_preds")