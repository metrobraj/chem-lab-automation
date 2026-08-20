import math
# this page holds all formulas

def nernst(ecell0, zn, cu):
    return (ecell0 - (0.01305)*math.log(zn/cu))

def gibbs(ecell0, zn, cu):
    return ((-2)*(96500)*(nernst(ecell0, zn, cu)))

