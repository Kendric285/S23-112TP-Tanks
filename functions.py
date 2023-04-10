from cmu_graphics import *
import decimal,math


def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def add(a,b):
    return a + b

def distance(x1, y1, x2, y2):
    x = x2 - x1 
    x_two = x*x
    y = y2 - y1
    y_two = y*y
    d = math.sqrt(x_two + y_two)
    return d