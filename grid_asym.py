import numpy as np
import argparse
import csv
from scipy.optimize import curve_fit
from scipy.signal import argrelextrema as ext
import matplotlib.pyplot as plt
##########################Documentation###########################
## (1) LOAD a list of the grid files                            ##
## (2) SAVE data into dictionary with key=grid positon          ##
## (3) FIND local mins of entire FES                            ##
## (4) FIT change in local mins to -exponential function        ##
## (5) RETURN best fit data parameters                          ##
## (ALT) PICK random points instead of local mins               ##
##################################################################


#Load a list with the names of the grid files to read in
parser=argparse.ArgumentParser()
parser.add_argument("-grid_list","--grid_list",help="list of grids")
parser.add_argument("-title","--title",help="title of plot")
args=parser.parse_args()

with open(str(args.grid_list)) as l:
    grid_list= l.read().splitlines()
l.close()

metad=[]
der=[]
#print(grid_list.split('\'))
for grid in grid_list:
    m,d=[],[]
    f=open(grid,'r')
    res_list = [i for i in f.readlines()[5:]]
    for row in res_list:
        s=row.split()[0]
        m.append(float(row.split()[1]))
        d.append(float(row.split()[2]))
    metad.append(m)
    der.append(m)


spacing=np.arange(0,float(s)*100,1)
dict_metad=dict.fromkeys(spacing)
dict_der=dict.fromkeys(spacing)

for n in range(len(spacing)):
    dict_metad[spacing[n]]=[i[n] for i in metad]
    dict_der[spacing[n]]=[i[n] for i in der]

#Find Deepest Well Value
avg=[]
for key,elem in dict_der.items():
    avg.append(np.mean(dict_metad[key]))
max_index=spacing[avg.index(np.max(avg))]

print(max_index)
print(dict_metad[max_index])

def log(x,a,b):
    return a*np.log(x) + b
x=np.arange(10,10*(len(dict_metad[0])+1),10)
y=np.array(dict_metad[max_index])

popt,pcov=curve_fit(log,x,y)
title =  str(args.title) + " well " + str(max_index/100) + "nm"

fig, (figure)= plt.subplots(nrows=1, figsize=(8,5))
figure.scatter(x,y*0.239006,color='black')
#plt.plot(x,log(x,*popt))
plt.ylim([0,20])
plt.xticks(x)
plt.title(title)
plt.xlabel("ns")
plt.ylabel("kcal/mol")
plt.savefig("deepest_well.png")

#############  CHECK ASYMPTOTIC BEHAVIOR OF RANDOM POINTS ################
#Create a list of Values + Deepest Well Value to Curve Fit to
#keys_for_fit=[]
#for i in range(50):
#   keys_for_fit.append(np.round(np.random.uniform(200,600),0))
#if (max_index in keys_for_fit) == False:
#    keys_for_fit.append(max_index)=
###########################################################################
"""
test,keys_for_fit=[],[]
for key,elem in dict_metad.items():
    test.append(dict_metad[key][0])

#CurveFit
def exponentail(x,a,b,c):
    return a*np.exp(-x/b) + c

xdata=np.arange(0,len(grid_list), 1)
all_tau=[]
#popt,pcov=curve_fit
for key in ext(np.array(test),np.greater)[0]:
    #print(dict_metad[key]-np.mean(dict_metad[key]))
    popt,pcov=curve_fit(exponentail, xdata, dict_metad[key]-np.mean(dict_metad[key]))
    #print(popt[1],popt)
    all_tau.append(popt[1])
print(all_tau)"""
