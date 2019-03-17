import math
import numpy as np
from matplotlib import pyplot as plt

#Put function here
def f(x):
    #Eg. (e^-x) - x = 0  ----> x = e^-x
    return math.exp(-x)

    #Eg. 6.3 x^3 - 6x^2 + 11 - 6.1 init_guess = 3.5
    # return (6*(x**2) - 12*x + 6.1) / (x**2)

init_guess = 0
xold = [init_guess]
list_xnew = []
iterate = 0
ea = 999999
es = 0.001

# print()

while(ea >= es and iterate < 100):
    if(iterate == 0):
        print("X", +iterate, "=",xold[iterate]," Ea = - ")
    else:
        xnew = f(xold[iterate-1])
        list_xnew.append(xnew)
        ea = abs(((xnew - xold[iterate-1]) / xnew)* 100)
        print("X",+iterate,"=",xnew," Ea = ",+ea)
        xold.append(xnew)
    iterate += 1
list_xnew.append(f(xold[len(xold)-1]))


#Graphical Interpretation
x_val = np.linspace(0,2)
fx1 = np.vectorize(f)(x_val)
fx2 = np.vectorize(lambda x:x)(x_val)
plt.plot(xold,list_xnew)
plt.plot(x_val,fx1)
plt.plot(x_val,fx2)
plt.axhline(color='black')
plt.plot(xold[len(xold)-1], list_xnew[len(list_xnew)-1],"o")
plt.grid()
plt.show()