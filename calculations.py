import math
# this page holds all formulas

def nernst(ecell0, zn, cu, T):
    return (ecell0 - ((8.314*T)/(2*96500))*math.log(zn/cu))

def gibbs(ecell0, zn, cu):
    return ((-2)*(96500)*(nernst(ecell0, zn, cu)))

def enthalpy():
    return