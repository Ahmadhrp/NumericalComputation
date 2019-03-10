import math

# Put function here
def fn(temperature):

    #Eg. 5.21 Heat of dry air related to temperature
    try:
        return 0.99403 + ((1.671 * math.pow(10, -4)) * temperature) + (
                (9.7215 * math.pow(10, -8)) * math.pow(temperature, 2)) \
               - ((9.5838 * math.pow(10, -11)) * math.pow(temperature, 3)) + (
                       (1.9520 * math.pow(10, -14)) * math.pow(temperature, 4)) - 1.1
    except ZeroDivisionError:
        return math.nan

# ============================= Bisection Method ==================================

#Calc new Xr
def calc_xr(lb,ub):
    return (lb + ub)/2

#Evaluate sign changes and change interval value
def newInterval(function,lb,ub,mid,isChecking):
    if(isChecking):
        return 1 if function(lb) * function(ub) < 0 else 0
    return [lb,mid] if function(lb) * function(mid) < 0 else [mid,ub]

# =================================================================================

#parameters
iterate = 0
ea = 999999
es = 0.5
x1 = 0
xu = 1200
xr_old = [0]

#bisection
while(ea >= es and iterate < 100):
    if(iterate == 0):
        xr_old[iterate] = calc_xr(x1,xu)
        x1,xu = newInterval(fn,x1,xu,xr_old[iterate],0)
        print("Xr ", +iterate + 1, " = ", +xr_old[iterate],", Ea = -")
    else:
        new_xr = calc_xr(x1,xu)
        x1,xu = newInterval(fn, x1, xu, new_xr,0)
        ea = abs(((new_xr - xr_old[iterate-1]) / new_xr) * 100)
        print("Xr ",+iterate+1," = ",+new_xr,", Ea = ",+ea)
        xr_old.append(new_xr)
    iterate += 1

# plotting
# x_val = np.linspace(0,1200)
# ft = np.vectorize(fn)(x_val)
# plt.plot(x_val, ft, label='Cp')
# plt.plot(xr_old[len(xr_old)-1], fn(xr_old[len(xr_old)-1]),"o")
# plt.grid(True)
# plt.title('Specific Heat of Dry Air in relation with Temperature')
# plt.show()