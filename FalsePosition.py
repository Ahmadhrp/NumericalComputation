import math
# np.warnings.filterwarnings('ignore')

# Put function here
def f(x):

    #Eg. Bungee jumping related to mass
    try:
        return math.sqrt(9.81 * x / 0.25) * math.tanh(math.sqrt(9.81 * 0.25 /x) * 4) - 36
    except ZeroDivisionError:
        return math.nan

# ============================= False Position Method ==================================

#Calc new Xr
def calc_xr(lb,ub):
    return ub - (f(ub)*(lb - ub)) / (f(lb) - f(ub))

#Evaluate sign changes and change interval value
def newInterval(lb,ub,mid,isChecking):
    if(isChecking):
        return 1 if f(lb) * f(ub) < 0 else 0
    return [lb,mid] if f(lb) * f(mid) < 0 else [mid,ub]

# =================================================================================

#Parameters
iterate = 0
ea = 999999
es = 0.5
x1 = 50
xu = 200
x_list = [0]

# Bisection
while(ea >= es and iterate < 50):
    if(iterate == 0):
        x_list[iterate] = calc_xr(x1,xu)
        x1,xu = newInterval(x1,xu,x_list[iterate],0)
        print("Xr ", +iterate + 1, " = ", +x_list[iterate],", Ea = -")
    else:
        new_xr = calc_xr(x1,xu)
        x1,xu = newInterval(x1,xu,new_xr,0)
        ea = abs(((new_xr - x_list[iterate-1]) / new_xr) * 100)
        print("Xr ",+iterate+1," = ",+new_xr,", Ea = ",+ea)
        x_list.append(new_xr)
    iterate += 1

