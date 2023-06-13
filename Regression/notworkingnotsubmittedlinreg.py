import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

#Still doesnt work, worked on it with robby, kylem kito, alex, and others possibly i forget
class LinearRegression():
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        self.num_iterations=1000

    def fit(self,X,y):
        if(X.shape[0]>1):
            #Gradient Descent for Multilinear Regression
            self.coef_, self.intercept_ = self._multi_linear_regression(X,y)
        else:
            #Simple Linear Regression
            self.coef_, self.intercept_ = self.simple_linear_regression(X, y)

    def predict(self, testX):
        return np.dot(testX * self.coef_) + self.intercept_

    #from kito
    def simple_linear_regression(self, X, y):
        N = len(X)
        x_mean = X.mean()
        y_mean = y.mean()

        b1_num = ((X - x_mean) * (y - y_mean)).sum()
        b1_den = ((X - x_mean) ** 2).sum()
        beta = b1_num / b1_den

        alpha = y_mean - (beta * x_mean)

        reg_line = 'y = {} + {}β'.format(alpha, round(beta, 3))

        return beta, alpha

    #not used
    def _corr_coef(self, X, y):
        N = len(X)

        num = (N * (X * y).sum()) - (X.sum() * y.sum())
        den = np.sqrt((N * (X ** 2).sum() - X.sum() ** 2) * (N * (y ** 2).sum() - y.sum() ** 2))
        R = num / den
        return R

    #from kyle and robby
    def _multi_linear_regression(self, X, y, alpha=0.01):
        if isinstance(X, pd.DataFrame) or isinstance(X, pd.Series):
            X = X.to_numpy()
        if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
            y = y.to_numpy()

        X = np.c_[np.ones((len(X), 1)), X]

        m = len(X)
        num_features = X.shape[1]
        print('sample count:', m)
        print('feature count:', num_features)

        theta = np.zeros((num_features, 1))

        for iteration in range(self.num_iterations):
            y_hat = np.dot(X, theta)

            error = y_hat - y
            # Transformed X * Error
            gradv = np.dot(X.T, error)

            theta = theta - alpha * gradv / m

        a = theta[0, 0]
        b = list(theta[1, :])
        return b,a

    #not Used copied from the website
    def _batch_gradient_decent(self, X, y):
        if isinstance(X, pd.DataFrame) or isinstance(X, pd.Series):
            X = X.to_numpy()
        if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
            y = y.to_numpy()
        # 1. Generate w0 w1 and alpha
        w0 = 0
        w1 = 0
        a = .004
        MSE = np.array([])

        for i in range(1, 11):

            # 2. Find prediction value
            y_pred = np.array([])
            error = np.array([])
            error_x = np.array([])

            for _ in X:
                y_pred = np.append(y_pred, (w0 + w1 * i))
            error = np.append(error, y_pred - y)
            error_x = np.append(error_x, error * X)
            MSE_val = (error ** 2).mean()
            MSE = np.append(MSE, MSE_val)

            # 3 Calculate Error and MSE
            w0 = w0 - a * np.sum(error)
            w1 = w1 - a * np.sum(error_x)
        return w0, w1



if __name__ == '__main__':
    test_model = LinearRegression()
    test_x = np.array([1, 3, 5])
    test_y = np.array([5, 12, 18])

    test_model.fit(test_x, test_y)
    preds = test_model.predict([1,3,5])

    df = pd.read_csv("bitcoin.csv")

    X = df["Open"]
    y = df["Close"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=6, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)
    yPred = model.predict((X_test))
    print(f"Simple: {preds}, Multi: {yPred}")

