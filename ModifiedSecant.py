import math
import numpy as np
from matplotlib import pyplot as plt

#Put function here
def f(x):

    #Ex. 6.3 x^3 - 6x^2 + 11 - 6.1 x0 = 3.5 perturb = 10^-6
    return x ** 3 - 6 * (x ** 2) + 11 * x - 6.1

    #x_min1 = 3, x0 = 4
    # return (2 * math.pow(x,3)) - (11.7 * math.pow(x,2)) + (17.7 * x) - 5

    #Bungee jumping related to mass x0 = 50 perturb = 10^-6
    # return math.sqrt(9.81 * x / 0.25) * math.tanh(math.sqrt(9.81 * 0.25 /x) * 4) - 36

#============================= Modified Secant ===============================

def ModSecant(xi,perturb):
    return xi - ((perturb * xi) * f(xi)) / (f(xi + (perturb * xi)) - f(xi))

#=============================================================================

iterate = 0
ea = 99999
es = 0.001
x0 = 3.5
perturb = 0.000001
x_list = [x0]

print(math.pow(10,-6))
while(ea >= es and iterate < 100):
    if(iterate == 0):
        print("X",+iterate,"=",x_list[iterate],"Ea = -")
    else:
        new_xi = ModSecant(x_list[iterate-1],perturb)
        ea = abs((new_xi - x_list[iterate-1]) / new_xi) * 100
        print("X", +iterate, "=", new_xi, "Ea =",+ea)
        x_list.append(new_xi)
    iterate += 1

#Graphical Interpretation
x_val = np.linspace(0,5)
fx = np.vectorize(f)(x_val)
plt.plot(x_val,fx)
plt.grid()
plt.show()