import math
# this page holds all formulas

def nernst(ecell0, zn, cu, T):
    return (ecell0 - ((8.314*T)/193000)*math.log(zn/cu))

def gibbs(ecell0, zn, cu, T):
    return ((-2)*(96500)*(nernst(ecell0, zn, cu, T)))

def free_energy():
    
    print("Need Free-energy change yeah?")
    print("Well, you'll need to provide Cu and Zn concentrations(separate by commas, in order)")
    #take input, split string, convert input values to float
    
    cuzn = input()
    cu, zn = cuzn.split(", ")
    cu = float(cu)
    zn = float(zn)

    #take ecell nought value
    print("Thank you, Ecell nought values(as calculated by nernst equation) at 30 deg")
    ecell = input()
    ecell30, ecell50 = ecell.split(", ")
    ecell30 = float(ecell30)
    ecell50 = float(ecell50)
    #gives free energy change value calculated from calculations.py
    kgibb30 = (gibbs(ecell30, zn, cu, 303))/1000
    kgibb50 = (gibbs(ecell50, zn, cu, 323))/1000

    print(f"Free-energy change at 30 C is {kgibb30:.3f} kJ/mol")
    print(f"Free-energy change at 50 C is {kgibb50:.3f} kJ/mol")


def enthalpy():
    return