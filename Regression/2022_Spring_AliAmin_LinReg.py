import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

#Still doesnt work, worked on it with robby, kyle, kito, alex, and others possibly i forget
class LinearRegression:
    def __init__(self):
        self.coeff = []
        self.intercept = 0

    def fit(self, X, y, alpha=.01, num_iterations=10000):
        '''
        Create the regression line on the data
        '''
        if isinstance(X, pd.DataFrame) or isinstance(X, pd.Series):
            X = X.to_numpy()
        if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
            y = y.to_numpy()

        #Array full of ones the shape of X concatinated with X
        X = np.c_[np.ones((len(X), 1)), X]

        m = len(X)
        num_features = X.shape[1]
        print('sample count:', m)
        print('feature count:', num_features)
        theta = np.zeros((num_features, 1))

        for i in range(num_iterations):
            y_hat = np.dot(X, theta)
            error = y_hat - y
            gDescent = np.dot(X.T, error)
            theta = theta - (alpha * (gDescent / m))

        self.intercept = theta[0, 0]
        self.coeff = list(theta[1,:])

    def predict(self, X):
        '''
        Predict the associated y of the x provided on the regression line created in the fitting process
        '''
        return np.dot(X, self.coeff) + self.intercept

    def get_coeff(self):
        '''
        Returns the coeffecient or 'm' of the regression's formula, y = mx+b
        '''
        return self.coeff

    def get_intercept(self):
        '''
        Returns the y-intercept or 'b' of the regression's formula, y = mx+b
        '''
        return self.intercept

if __name__ == '__main__':
    dk = pd.read_csv('housing_preds.csv')
    df = pd.read_csv('housing_data.csv')
    df = df.dropna()

    encoder1 = OrdinalEncoder()
    encoder2 = OrdinalEncoder()
    encoder1.fit(df[['ocean_proximity']])
    df['ocean_proximity'] = encoder1.transform(df[['ocean_proximity']])
    df['ocean_proximity'].value_counts()

    y = df["median_house_value"]
    X = df.drop('median_house_value', axis='columns')

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)
    yPred = model.predict((X_test))
    print(yPred)
    
