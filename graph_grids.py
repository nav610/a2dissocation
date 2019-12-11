import argparse
import matplotlib.pyplot as plt
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument("-grid_list","--grid_list",help="list of grids")
parser.add_argument("-title", "--title",help="title")
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

x = np.arange(0,8.02,.01)

fig, (figure)= plt.subplots(nrows=1, figsize=(8,5))
for file in metad:
    figure.plot(x,np.array(file)*0.239006,color='black')

plt.title(args.title)
plt.xlabel("ns")
plt.ylabel("kcal/mol")
plt.savefig("gridsgraphed.png")
