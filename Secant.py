import math
import numpy as np
from matplotlib import pyplot as plt

#Put function here
def f(x):

    #Ex. 6.3 x^3 - 6x^2 + 11 - 6.1 x0 = 3.5 x-1 = 2.5
    return x ** 3 - 6 * (x ** 2) + 11 * x - 6.1

    #x_min1 = 3, x0 = 4
    # return (2 * math.pow(x,3)) - (11.7 * math.pow(x,2)) + (17.7 * x) - 5

#================================ Secant  ====================================

def Secant(xi,xi_min1):
    return xi - (f(xi) * (xi - xi_min1)) / (f(xi) - f(xi_min1))

#=============================================================================


iterate = 0
ea = 99999
es = 0.001
x0 = 3.5
x_min1 = 2.5
x_old = [x_min1,x0]
x_new = []

while(ea >= es and iterate < 100):
    if(iterate == 0):
        print("X",+iterate,"=",x_old[iterate],"Ea = -")
    else:
        new_xi = Secant(x_old[iterate],x_old[iterate-1])
        x_new.append(new_xi)
        ea = abs((new_xi - x_old[iterate]) / new_xi) * 100
        print("X", +iterate, "=", new_xi, "Ea =",+ea)
        x_old.append(new_xi)
    iterate += 1

#Graphical Interpretation
x_val = np.linspace(0,5)
fx = np.vectorize(f)(x_val)
# plt.xlim(-1,5)
plt.plot(x_val,fx)
plt.axhline(color='black')
plt.grid()
plt.show()