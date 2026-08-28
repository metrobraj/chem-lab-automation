#Exp - 4: Estimation of fe using potentiometry

import math
import matplotlib.pyplot as plt

N_KMNO4 = 0.05
v_beaker = 20

#DEVELOPER TESTING TOOLS
#=================================================================================================================
EMF_val = {1:0.370,2:0.382,3:0.409,4:0.428,5:0.462,6:1.036,7:1.078,8:1.090,9:1.096,10:1.100}

t2_vol = [4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0,6.2,6.4]
t2_emf = [0.430,0.434,0.441,0.447,0.456,0.473,0.509,0.869,1.022,1.035,1.050,1.057,1.066]
#=================================================================================================================
de = []
avg_vol = []
dedv = []
skips = 0.2
#READINGS
n = int(input("Enter the number of readings taken for titration-I:\n"))
#FIRST TABLE INPUT:
def get_emf():
    
    for i in range(n):
        data = input(f"Please enter the readings for vol. {i+1}:(Reading by potentiometer)\n")
        EMF_val[i+1] = float(data)
#DEVELOPER TOOL TESTING
if n!=0:get_emf()

#SECOND TITRATION
def get_emf2():
    global skips,a,b
    a = float(input("Enter the starting volume of KMnO4 for titration-II:\n"))#4
    b = float(input("Enter the end value for titration-II:\n"))#6.2

    #value of dv
    skips = float(input("Enter the increment value of volume:(e.g 0.2 for 4.0 4.2 4.4)"))
    while a<b+0.1:
            data2 = input(f"Please enter the readings at volume {a:.2f}: ")
            t2_vol.append(a)
            t2_emf.append(data2)
            a+=skips
#DEVELOPER TOOL TESTING
if n!=0:get_emf2()
#SECOND TABLE CALCULATIONS
def calc_dedv():
    global skips
    for i in range(1,int(len(t2_vol))):
        a = float(t2_emf[i-1])
        b = float(t2_emf[i])
        de.append(-a+b)
        avg_vol.append((float(t2_vol[i-1])+float(t2_vol[i]))/2)

    for i in range(len(de)):
        #dedv.append(de[i]/avg_vol[i])
        dedv.append(de[i]/skips)

calc_dedv()
#PLOT GRAPH
def plot_emf():
    plt.figure()
    plt.plot(EMF_val.keys(),EMF_val.values(),marker = ".")
    plt.grid()
    plt.figure()
    plt.plot(avg_vol,dedv,marker = ".")
    plt.grid()
    plt.show()


# normality(final result calculation)
def normality():
    peak_dedv = max(dedv)
    peak_vol = avg_vol[dedv.index(peak_dedv)]
    print(f"The peak volume of kMnO4 graph is at {peak_vol:.3f} ml \n del E/del V at this point is {peak_dedv:.3f}.")
    peak_vol=float(input("Enter volume of KMnO4 from Plot-2: "))
    n = (0.05*peak_vol)/20
    Fe1 = n*55.85
    Fe100 = Fe1*0.1
    print(f"Normality of steel sample solution: {n:.4f} N")
    print(f"Amount of Fe present in 1L of sample solution: {Fe1:.4f} grams in 1L")
    print(f"Amount of Fe present in 100mL of sample solution: {Fe100:.4f} grams in 100mL")


#RESULTS DISPLAY
def results():
    print("Values of delta E: ")
    for i in range(len(de)):
        print(f"{de[i]:.3f}",end=',')
    print()
    print("Values of delta E/ delta V:")
    for i in range(len(dedv)):
        print(f"{dedv[i]:.3f}",end=',')
    print()
    print("Average Volume: ")
    for i in range(len(avg_vol)):
        print(f"{avg_vol[i]:.3f}",end=',')
    print()
    normality()


results()
plot_emf()

