#Experiment 2 - Calculating rate,order and molecularity using ester hydrolysis

import math
import matplotlib.pyplot as plt

#Value recorded by titration
Vol_NaOH = []

#Values of V_infinity - v_t
v_i = []

#ln(V_infi-V_t) cz x axis in graph
lnv = []

#Values of k at different time
rate_k = []

#To get data from user
def get_values():
    for i in range(5):
        Vol_NaOH.append(float(input(f"Enter value at T = {i*10}\n")))
    Vol_NaOH.append(float(input(f"Enter value at T = infinity\n")))
    

#Calculation based on the values collected from user
def calc_rate():

    get_values()
    n = len(Vol_NaOH) # n= 5

    #calculating v_infi - v_t
    for i in range(n-1):
        v_i.append(Vol_NaOH[n-1]-Vol_NaOH[i])
        lnv.append(math.log10(v_i[i]))
        #print("log(V_i - V_t) = lnv[i]") -- #uncomment to display log values, x axis of graph
    
    
    #print(v_i)
    #Adding values to rate list, i should go from 1 to n-1 i.e. 4 as at t = 0, no k
    
    #Adding calculated k values
    for i in range(1,n-1):
        rate_k.append((2.303/(i*10))*math.log10(v_i[0]/(v_i[i]))) 

def plt_graph(x:list, y:list):
    plt.plot([x[0],x[4]],[y[0],y[4]])
    plt.plot(x,y,'ro',label = "Data Points")
    plt.ylabel("log(V_infi - V_t)")
    plt.xlabel("Time (in min)")
    plt.show()

#printing output
sum = 0
def print_result():
    global sum
    calc_rate()
    for i in range(len(rate_k)):
        print(f"Rate constant at T = {i*10}: {rate_k[i]:.2e} ")
        sum+=rate_k[i]
    print(f"Average Rate constant: {sum/len(rate_k):.2e}")
    #print("Slope of graph: ",(lnv[4]-lnv[0]/40)) -- gives wrong assumptions according to the  readings i had
    plt_graph([0,10,20,30,40],lnv)
        
print_result()