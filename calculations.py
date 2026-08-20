import math
# this page holds all formulas

def nernst1():
    return emm-(0.0595/n)(math.log(gamma*c, 10))

def nernst():
    return ecell0 - (0.01305)*math.log(zn/cu)

def gibbs():
    return (-n)*(96500)*(nernst())

