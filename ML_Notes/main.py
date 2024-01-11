import numpy as np
import matplotlib.pyplot as plt

'''
Further ToDos:
    Make a function to run linear regression with different rates and iterations
    Make a function to output the correct number of iterations and learning rate to use
    Function to output the optimal graph
'''


class LogisticRegression:
    def __init__(self, learning_rate: float = 0.05, iterations: int = 5):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = lambda: None
        self.bias = lambda: None
        self.cost = []

    def fit(self, X, y):
        num_samples, num_features = X.shape

        # initialize the weights and bias
        self.weights = np.zeros(num_features)
        self.bias = 0

    def feed_forward(self, X):
        # predict using trained values
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred

    def sigmoid(self, X) -> float:
        return 1 / (1 + np.exp(np.e, -self.feed_forward(X)))


class LinearRegression:
    def __init__(self, learning_rate: float = 0.05, iterations: int = 5):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = lambda: None
        self.bias = lambda: None
        self.cost = []

    def fit(self, X, y):
        num_samples, num_features = X.shape

        # initialize the weights and bias
        self.weights = np.zeros(num_features)
        self.bias = 0

        # gradient descent algorithm
        for i in range(self.iterations):
            # predict the output of the initial weights
            y_pred = self.feed_forward(X)

            # Cost Calculation
            cost = (1 / (2 * num_samples)) * np.sum((y_pred - y) ** 2)
            self.cost.append(cost)

            # calculate the gradient values
            dw = (1 / num_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / num_samples) * np.sum(y_pred - y)

            # update the weights and biases
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            print(f"Weight: {self.weights} Bias: {self.bias} Cost: {cost}")

    def feed_forward(self, X):
        # predict using trained values
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred


class OptimalValueDeterminer:
    """
    We want to determine when the cost is the lowest, so we need to store the cost
    The stored cost for different iterations
    """

    def __init__(self, learning_rates: float = None, iterations_options: int = None):

        if learning_rates is None:
            learning_rates = [0.1, 0.05, 0.01]
        self.learning_rates = learning_rates

        if iterations_options is None:
            iterations_options = [50, 100, 250, 500]
        self.iteration_options = iterations_options

    def run_regression(self, X):
        # run the different combination of regression
        for i in self.learning_rates:
            for j in self.iteration_options:
                linear_regression = LinearRegression(learning_rate=i, iterations=j)
                linear_regression.fit(X)

    def find_optimal(self):
        # find the most optimal combination and return it
        pass


def main():
    linear_regression = LinearRegression(learning_rate=0.01, iterations=40)
    X = np.array([[4], [6], [10], [12], [14]])
    y = np.array([9, 17, 20, 21, 29])

    # Run the fit function
    linear_regression.fit(X, y)

    # Y output predictions
    y_pred = linear_regression.feed_forward(X)

    # plot the data points and the linear regression line
    plt.scatter(X, y)
    plt.plot(X, y_pred)
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()

    # plot the cost data
    plt.plot(linear_regression.cost[1:])
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.show()


if __name__ == "__main__":
    main()
