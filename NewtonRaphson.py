import math
import numpy as np
from matplotlib import pyplot as plt

#Put function here
def f(x):
    # Eg. (e^-x) - x = 0 x0=0
    # return math.exp(-x) - x

    # Ex. 6.3 x^3 - 6x^2 + 11 - 6.1 x0 = 3.5
    return x**3 - 6 * (x**2) + 11 * x - 6.1

#Function Derivatives using power rule
def df(x):
    # Eg. (e^-x) - x = 0
    # return -(math.exp(-x)) - 1

    # Ex. 6.3 x^3 - 6x^2 + 11 - 6.1
    return 3*(x**2) - 12*x + 11

def tangen_line(ln_start,ln_end):
    points = np.linspace(ln_start,ln_end)
    y = df(ln_start) * (points - ln_start) + f(ln_start)
    plt.plot(points, y, '--k')
    # return df(0.5) * (val - 0) + f(0.5)

#=================================== Newton Raphson ==================================

# Xi + 1 calculation
def NewtonRaphson(x):
    return x - f(x) / df(x)

#=====================================================================================

iterate = 0
initial_guess = 3.5
es = 0.001
ea = 99999
x_old = [initial_guess]
x_new = []

while(ea >= es and iterate < 100):
    if(iterate == 0):
        print("Xi",+iterate,'=',+x_old[iterate],'Ea = -')
    else:
        new_xi = NewtonRaphson(x_old[iterate-1])
        x_new.append(new_xi)
        ea = abs((new_xi - x_old[iterate-1]) / new_xi) * 100
        print("Xi", +iterate, '=', +new_xi, 'Ea =',+ea)
        x_old.append(new_xi)
    iterate += 1
x_new.append(NewtonRaphson(len(x_old)-1))

# print("X old =",x_old)
# print("X new =",x_new)
# print("True root value =",f(0.56714329))

#Graphical Interpretation
x_val = np.linspace(0,5)
fx = np.vectorize(f)(x_val)
# plt.ylim(-1.5,1.5)
# plt.xlim(-0.5,2)
plt.axhline(color='black')
# plt.plot(x_val,fx,label='f(x) = x^10 - 1')
plt.plot(x_val,fx,label='f(x) = 6.3 x^3 - 6x^2 + 11 - 6.1')

#Draw tangen line steps untuk stoping criterion
for i in range(len(x_old)-1):
    tangen_line(x_old[i],x_new[i])

plt.plot(.56714329, f(.56714329),"o", label="Root true value")
plt.grid()
plt.legend()
plt.title('Newton Raphson Method')
plt.show()