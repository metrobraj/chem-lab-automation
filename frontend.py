import units
import calculations

print("Need Free-energy change yeah?")
print("well, you'll need to gimme Cu and Zn concentrations(separate by commas, in order)")

cuzn = input()
cu, zn = cuzn.split(", ")
cu = float(cu)
zn = float(zn)

print("thanks, Ecell nought value(as calculated by nernst equation) please")
ecell0 = float(input())

gibb = calculations.gibbs(ecell0, zn, cu)
print("your free energy change is", gibb)