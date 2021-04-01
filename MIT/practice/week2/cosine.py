import numpy as np
import math as math

# This is the calc of the angle btween two planes


def calcAngle(first, second):
    top = abs(np.dot(np.array(first), np.array(second)))
    bottomL = 0
    for fi in first:
        bottomL += fi**2
    bottomR = 0
    for sec in second:
        bottomR += sec**2
    bottom = math.sqrt(bottomL * bottomR)
    return math.degrees(math.acos(top/bottom))


#print(calcAngle([1, 1, 1], [2, 2, 2]))
print(calcAngle([2, 2, 2], [-2, -3, 7]))
