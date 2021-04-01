import numpy as np
from week2 import calcPoints


def perceptron(dataset, t):
    theta = np.zeros(len(dataset[0][0]))
    theta0 = 0
    for i in range(t):
        for dataPoint in dataset:
            y = dataPoint[1]
            x = np.array(dataPoint[0])
            if((y * (theta.T @ x + theta0)) <= 0):
                print("Mistake on point:  ", x,
                      " with theta: ", theta, " ", theta0)
                theta = theta + (y*x)
                theta0 = theta0 + y
            else:
                print("Correct on point: ", x,
                      " with theta: ", theta, " ", theta0)
    return theta, theta0
