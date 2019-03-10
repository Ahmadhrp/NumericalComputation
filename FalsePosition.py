import math
# np.warnings.filterwarnings('ignore')

# Put function here
def fn(mass):

    #Eg. Bungee jumping related to mass
    try:
        return math.sqrt(9.81 * mass / 0.25) * math.tanh(math.sqrt(9.81 * 0.25 /mass) * 4) - 36
    except ZeroDivisionError:
        return math.nan

# ============================= False Position Method ==================================

#Calc new Xr
def calc_xr(function,lb,ub):
    return ub - (function(ub)*(lb - ub)) / (function(lb) - function(ub))

#Evaluate sign changes and change interval value
def newInterval(function,lb,ub,mid,isChecking):
    if(isChecking):
        return 1 if function(lb) * function(ub) < 0 else 0
    return [lb,mid] if function(lb) * function(mid) < 0 else [mid,ub]

# =================================================================================

#Parameters
iterate = 0
ea = 999999
es = 0.5
x1 = 50
xu = 200
xr_old = [0]

# Bisection
while(ea >= es and iterate < 50):
    if(iterate == 0):
        xr_old[iterate] = calc_xr(fn,x1,xu)
        x1,xu = newInterval(fn,x1,xu,xr_old[iterate],0)
        print("Xr ", +iterate + 1, " = ", +xr_old[iterate],", Ea = -")
    else:
        new_xr = calc_xr(fn,x1,xu)
        x1,xu = newInterval(fn,x1,xu,new_xr,0)
        ea = abs(((new_xr - xr_old[iterate-1]) / new_xr) * 100)
        print("Xr ",+iterate+1," = ",+new_xr,", Ea = ",+ea)
        xr_old.append(new_xr)
    iterate += 1

