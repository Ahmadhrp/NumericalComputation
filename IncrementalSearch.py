import numpy as np
import math
# np.warnings.filterwarnings('ignore')

# Put function here
def f(x):

    #Eg. Bungee jumping related to mass
    try:
        return math.sqrt(9.81 * x / 0.25) * math.tanh(math.sqrt(9.81 * 0.25 /x) * 4) - 36
    except ZeroDivisionError:
        return math.nan

# ============================= Incremental Search Method ==================================

#Evaluate sign changes until the end of interval
def checkSign(lb,ub):
    return 1 if f(lb) * f(ub) < 0 else 0

# =================================================================================

count = 0
points = []
x_val = np.linspace(50,200,100)
# print(x_val)

for i in range(len(x_val)-1):
    if checkSign(x_val[i],x_val[i+1]):
       points.append((x_val[i],x_val[i+1]))
       count +=1

print("Found",+count,"roots")
for coor in points:
    print(coor)
