import units
import calculations
#ask user for input
print("Need Free-energy change yeah?")
print("Well, you'll need to provide Cu and Zn concentrations(separate by commas, in order)")
#take input, split string, convert input values to float
cuzn = input()
cu, zn = cuzn.split(", ")
cu = float(cu)
zn = float(zn)
#take ecell nought value
print("Thank you, Ecell nought value(as calculated by nernst equation) please")
ecell0 = float(input())
#gives free energy change value calculated from calculations.py
gibb = calculations.gibbs(ecell0, zn, cu)
kgibb = gibb/1000
print(f"Your Free-energy change is {kgibb:.3f} kJ/mol")
