import numpy as np
from perceptron import perceptron
from week2 import calcPoints

# data = [([1, 1], 1), ([-1, -1], -1), ([0, 1], 1),
#       ([0, -1], -1), ([1, 0], 1), ([-1, 0], -1)]

data = [([-1, -1], -1), ([-1.38, -1.25], -1), ([-1, -2], -1),
        ([-2.4, -0.99], -1), ([-2.44, -0.49], -1), ([-1.64, -0.55], -1), ([-2, -1.35], -1), ([-1.56, -2.19], -1), ([-2.2, 0.37], -1), ([1, 2], 1), ([1.46, 2.25], 1), ([2, 2], 1), ([1.62, 1.47], 1), ([1, 1], 1), ([0.18, 0.39], 1), ([0.52, 1.57], 1), ([1.82, 0.23], 1), ([2.48, 0.97], 1), ([3.12, 1.67], 1), ([2.34, 1.71], 1), ([1.96, 1.25], 1), ([0.98, 0.45], 1), ([1.26, -0.71], 1)]


newTheta = perceptron(data, 2)
print("The hyperplane is: ", newTheta[0], "+ ", newTheta[1])

for point in data:
    print("Point: ", point[0])
    if(calcPoints(newTheta[0], point[0]) > 0):
        print(1)
    else:
        print(-1)
