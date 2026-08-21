import calculations
#ask user for input
print("Ready? [1] for yes, [2] for no")
while True:
    if int(input())==1:
        calculations.free_energy()
        break
    else: 
        print("alr, waiting for you")
        continue
