import math
#EMF CELL HAS BEEN FIXED. DANIEL CELL IS PENDING.

#we give the user 2 options, whether to opt for emf measured from various conc, or 
def emfcell():
    #taking concentration inputs first
    print("Ecell for [Zn] = 0.05M: ")
    ezn5=float(input())
    print("Ecell for [Zn] = 0.1M: ")
    ezn1=float(input())
    print("Ecell for [Cu] = 0.05M: ")
    ecu5=float(input())
    print("Ecell for [Cu] = 0.1M: ")
    ecu1=float(input())
    #calculate and print Em/m+ value, where Em/m+ = Ecell + Ecalomel
    emmzn5=ezn5+0.244
    emmzn1=ezn1+0.244
    emmcu5=ecu5+0.244
    emmcu1=ecu1+0.244
    print(f"Em/m+/V value for 0.05 M Zn: {emmzn5:.3f}")
    print(f"Em/m+/V value for 0.1 M Zn: {emmzn1:.3f}")
    print(f"Em/m+/V value for 0.05 M Cu: {emmcu5:.3f}")
    print(f"Em/m+/V value for 0.1 M Cu: {emmcu1:.3f}")
    print("==============================================")
    #calculate E0m/m+ from Nernst Eqn-1
    e0mmzn5 = emmzn5 - (0.02975)*(math.log(0.57*0.05, 10))
    e0mmzn1 = emmzn1 - (0.02975)*(math.log(0.485*0.1, 10))
    e0mmcu5 = emmcu5 - (0.02975)*(math.log(0.57*0.05, 10))
    e0mmcu1 = emmcu1 - (0.02975)*(math.log(0.485*0.1, 10))
    print(f"E0m/m+/V for 0.05M Zn: {e0mmzn5:.3f}")
    print(f"E0m/m+/V for 0.1M Zn: {e0mmzn1:.3f}")
    print(f"E0m/m+/V for 0.05M Cu: {e0mmcu5:.3f}")
    print(f"E0m/m+/V for 0.1M Cu: {e0mmcu1:.3f}")
    print("==============================================")
    #calculate average e0
    avgzn = (e0mmzn5+e0mmzn1)/2
    avgcu = (e0mmcu5+e0mmcu1)/2
    print(f"Average E0 for Zn: {avgzn:.3f}")
    print(f"Average E0 for Cu: {avgcu:.3f}")
    print("==============================================")

def danielcell():
    n

print("Enter [1] for EMF measured for various concentrations of M/Mn+ system")
print("Enter [2] for EMF of Daniel Cell observed")
n=int(input())
if(n==1):
    emfcell()
    print("Carry on to Daniel Cell?")
    print("Enter [1] for yes, [2] for no")
    if(int(input())==1):
        #FUNCTION FOR DANIEL CELL
        pass
    else:
        pass
else:
    #FUNCTION FOR DANIEL CELL
    pass