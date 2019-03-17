import math
import numpy as np
from matplotlib import pyplot as plt

#Put function here
def f(x):
    #Ex. 6.3 x^3 - 6x^2 + 11 - 6.1 x = 3.5 x-1 = 2.5 x-2 = 1.5
    return x ** 3 - 6 * (x ** 2) + 11 * x - 6.1
    # return x ** 2 - 20
    # return -2 * (x**4) + 2 * (x**3) - 16*(x**2) - 60*x + 100

#============================= Inverse Quadratic Interpolation =============================

def InverseQuadratic(x0,x1,x2):

    #x0 = x-2, x1 = x-1, x2 = x
    y0 = f(x0)
    y1 = f(x1)
    y2 = f(x2)

    # Lagrange Polinomial at y = 0
    L0 = (x0 * y1 * y2) / ((y0 - y1) * (y0 - y2))
    L1 = (x1 * y0 * y2) / ((y1 - y0) * (y1 - y2))
    L2 = (x2 * y1 * y0) / ((y2 - y0) * (y2 - y1))
    x_new = L0 + L1 + L2
    return x_new, x0, x1

#===========================================================================================

def PlotQuadratic(x0,x1,x2,val):
    y0 = f(x0)
    y1 = f(x1)
    y2 = f(x2)

    # Lagrange Polinomial
    L0 = (y0 * ((val - x1) * (val - x2))) / ((x0 - x1) * (x0 - x2))
    L1 = (y1 * ((val - x0) * (val - x2))) / ((x1 - x0) * (x1 - x2))
    L2 = (y2 * ((val - x0) * (val - x1))) / ((x2 - x0) * (x2 - x1))
    return L0+L1+L2

def plotInverseQuadratic(x0,x1,x2,val):
    y0 = f(x0)
    y1 = f(x1)
    y2 = f(x2)

    # Swap x for y Lagrange Polinomial
    L0 = (x0 * ((val - y1) * (val - y2))) / ((y0 - y1) * (y0 - y2))
    L1 = (x1 * ((val - y0) * (val - y2))) / ((y1 - y0) * (y1 - y2))
    L2 = (x2 * ((val - y0) * (val - y1))) / ((y2 - y0) * (y2 - y1))
    return L0+L1+L2

iterate = 0
x0 = 3.3
x1 = 3.8
x2 = 4.2
es = 0.001
ea = 99999
x_list = [x0,x1,x2]

while (ea >= es  and iterate < 100):
    if(iterate == 0):
        print("X-2 =",+x0,",X-1 =",+x1,",X =",+x2,"Ea = -")
    else:
        r0, r1, r2 = InverseQuadratic(x0, x1, x2)
        x_list.append(r0)
        ea = abs((r0 - r1) / r0) * 100
        print("X",+iterate,"=",+r0,"Ea =",+ea)
    iterate += 1

x_val = np.linspace(0,5)
y_val = np.linspace(-5,10)
fx = np.vectorize(f)(x_val)
quad = np.vectorize(PlotQuadratic)(x0,x1,x2,x_val)
inv_quad = np.vectorize(plotInverseQuadratic)(x0,x1,x2,y_val)
plt.plot(x_val,fx,color = 'blue')
plt.xlim(-1,6)
plt.ylim(-10,10)
plt.plot(x0,f(x0),"o",color = 'blue')
plt.plot(x1,f(x1),"o",color = 'blue')
plt.plot(x2,f(x2),"o",color = 'blue')
plt.plot(x_val,quad,'--',color = 'orange',label="fx")
plt.plot(inv_quad,y_val,'--',color = 'green',label="gx")
plt.axhline(color='black')
plt.title('Inverse Quadratic Interpolation')
plt.grid()
plt.legend()
plt.show()