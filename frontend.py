import calculations
#ask user for input
<<<<<<< Updated upstream
print("Enter [1] for free energy, [2] for average free energy at 40 degrees")
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
#gives free energy change value calculated from calculations.py
kgibb30 = (calculations.gibbs(ecell30, zn, cu, 303))/1000
kgibb50 = (calculations.gibbs(ecell50, zn, cu, 323))/1000

print(f"Free-energy change at 30 C is {kgibb30:.3f} kJ/mol")
print(f"Free-energy change at 50 C is {kgibb50:.3f} kJ/mol")


=======
print("Enter [1] for free energy change at 30 degrees and 50 degrees")
calculations.free_energy()
>>>>>>> Stashed changes
