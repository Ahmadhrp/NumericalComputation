import numpy as np
from matplotlib import pyplot as plt
import math

# Put function here
def fn(x):

    #Eg. Sin(10x) + Cos(3x)
    try:
        return math.sin(10*x)+ math.cos(3*x)
    except ZeroDivisionError:
        return math.nan

# plotting
x_val = np.linspace(3,6)
ft = np.vectorize(fn)(x_val)
plt.plot(x_val, ft, label='Cp')
plt.grid(True)
plt.title('Sin(10x) + Cos(3x)')
plt.show()