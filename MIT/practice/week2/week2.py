import numpy as np


def calcPoints(theta, point):
    newTheta = np.transpose(np.array(theta))
    newPoint = np.array(point)
    result = newTheta @ newPoint
    return result
