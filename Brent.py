import math
import numpy as np
from matplotlib import pyplot as plt

#Put function here
def f(x):
    # Ex. 6.3 x^3 - 6x^2 + 11 - 6.1 x = 3.5 x-1 = 2.5 x-2 = 1.5
    # return x ** 3 - 6 * (x ** 2) + 11 * x - 6.1

    return x ** 2 - 20
    # try:
    #     return 0.99403 + ((1.671 * math.pow(10, -4)) * x) + (
    #             (9.7215 * math.pow(10, -8)) * math.pow(x, 2)) \
    #            - ((9.5838 * math.pow(10, -11)) * math.pow(x, 3)) + (
    #                    (1.9520 * math.pow(10, -14)) * math.pow(x, 4)) - 1.1
    # except ZeroDivisionError:
    #     return math.nan

#================================== Brent's Method ====================================

def brents(a, b):
    fa = f(a)
    fb = f(b)
    es = 0.00001

    assert (fa * fb) <= 0, "No sign change on your interval, Choose another number"

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c, fc = a, fa

    bisect = True
    iterate = 0

    while iterate < 100 and abs(b - a) > es:
        if (iterate == 0):
            print("X", +iterate, "=", +b, "Ea = -")
        else:
            fa = f(a)
            fb = f(b)
            fc = f(c)

            if fa != fc and fb != fc:
                L0 = (a * fb * fc) / ((fa - fb) * (fa - fc))
                L1 = (b * fa * fc) / ((fb - fa) * (fb - fc))
                L2 = (c * fb * fa) / ((fc - fa) * (fc - fb))
                new = L0 + L1 + L2
                flag = "IQI"

            else:
                new = b - ((fb * (b - a)) / (fb - fa))
                flag = "Secant"

            if ((new < ((3 * a + b) / 4) or new > b) or
                    (bisect == True and (abs(new - b)) >= (abs(b - c) / 2)) or
                    (bisect == False and (abs(new - b)) >= (abs(c - d) / 2)) or
                    (bisect == True and (abs(b - c)) < es) or
                    (bisect == False and (abs(c - d)) < es)):
                new = (a + b) / 2
                bisect = True
                flag = "Bisection"

            else:
                bisect = False

            fnew = f(new)
            d, c = c, b

            if (fa * fnew) < 0:
                b = new
            else:
                a = new

            print("X", +iterate, "=", +new,"|",flag,"| Ea =", +abs(b - a))
            if abs(fa) < abs(fb):
                a, b = b, a

        iterate += 1

    return b, iterate

#===============================================================================

root,steps = brents(2,5)

