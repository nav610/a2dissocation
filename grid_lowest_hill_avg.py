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
y=np.array(dict_metad[max_index])*0.239006

f = open("hill_min.txt","a+")
f.write(str(args.title))
f.write(",")
f.write(str(np.mean(y)))
f.write(",")
f.write(str(np.std(y)))
f.write("\n")
