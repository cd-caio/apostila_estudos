import numpy as np
import plotly.graph_objects as go
import time
class LinearRegression():
    # y^ = b0 + b1*x1 + b2*x2
    def __init__(
        self, 
        learning_rate:float=0.001, 
        n_iterations=100
    ):
        self.learning_rate = learning_rate
        self.bias = 0
        self.weights = None
        self.n_iterations = n_iterations

    def fit(self, X:np.array, y:np.array):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        for _ in range(self.n_iterations):
            y_pred = np.dot(X, self.weights) + self.bias
            error = y_pred-y
            dw = (1/n_samples) * np.dot(X.T, (error))
            db = (1/n_samples) * np.sum(error)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db
        
        fig = go.Figure(data=[
            go.Scatter(x=X.reshape(1,-1)[0], y=y.reshape(1,-1)[0], mode='markers'),
            go.Scatter(x=X.reshape(1,-1)[0],y=self.predict(X))
        ])
        fig.show()

    def predict(self, X:np.array):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred
    
    def mse(self, y_test, predictions):
        return np.mean((y_test-predictions)**2)