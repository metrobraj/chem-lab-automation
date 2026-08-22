#Exp - 4: Estimation of fe using potentiometry

import math
import matplotlib.pyplot as plt

N_KMNO4 = 0.05
v_beaker = 20


EMF_val = {}

t2_vol = []
t2_emf = []

de = []
avg_vol = []
dedv = []

def get_emf():

    n = int(input("Enter the number of readings taken for titration-I:\n"))
    for i in range(n):
        data = input("Pleasde enter the readings as : (Vol of KMnO4) (Reading by potentiometer)\n").split()
        EMF_val[float(data[0])] = float(data[1])

    a = float(input("Enter the starting value for titration-II:\n"))#4
    b = float(input("Enter the end value for titration-II:\n"))#6.2

    while a<b:
            data2 = input(f"Pleasde enter the readings at volume {a:.2f}: ")
            t2_vol.append(a)
            t2_emf.append(data2)
            a+=0.2

def calc_dedv():

    for i in range(0,int(len(t2_vol)),2):
        de.append(-t2_emf[i]+t2_emf[i+1])
        avg_vol.append((t2_vol[i]+t2_vol[i+1])/2)

    for i in range(len(de)):
         dedv.append(de[i]/avg_vol[i])

     
def plot_emf():
    calc_dedv()
    plt.figure()
    plt.plot(EMF_val.keys(),EMF_val.values(),marker = ".")
    plt.figure()
    plt.plot(avg_vol,dedv,marker = ".")
    plt.show()

get_emf()
plot_emf()


