import random
import seaborn

data = [
    (1, 5.1),
    (2, 6.9),
    (3, 9.2),
    (4, 10.8),
    (5, 12.1),
    (6, 15.0),
    (7, 16.9),
    (8, 18.2),
    (9, 20.3),
    (10, 22.1)
]

def calcSumSquareErrors(f, data):
    sse = 0
    for point in data:
        res = point[1] - f(point[0])
        sse += res ** 2
    
    return sse

def calcMedian(m1, m2, b1, b2):
    slope = (m1 + m2) / 2
    intercept = (b1 + b2) / 2

    return lambda x: slope * x + intercept

def calcIntercept(slope, x1, y1):
    return -1 * slope * x1 + y1

startPoints = [random.choice(data), random.choice(data)]

slope = (startPoints[0][1] - startPoints[1][1])/(startPoints[0][0] - startPoints[1][0])

f = lambda x: slope * (x - startPoints[0][0]) + startPoints[0][1] # median line

m = ((slope, calcIntercept(slope, startPoints[0][0], startPoints[0][1])), lambda x: slope * x + calcIntercept(slope, startPoints[0][0], startPoints[0][1]))


while True:
    if abs(l - m) > abs(m - s):
        #between m and s
    else:
        #between l and m