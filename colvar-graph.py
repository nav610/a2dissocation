import matplotlib.pyplot as plt
import argparse
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument('-colvar', '--colvar', help='COLVAR File to Graph')
parser.add_argument('-title','--title',help='title of graph')
args = parser.parse_args()

f = open(args.colvar,'r')
data = [i for i in f.readlines()[1:]]

dt1=[]
metad=[]
for row in data:
    dt1.append(row.split()[1])
    metad.append(row.split()[2])

x = np.arange(0,len(dt1),100)
timescale=100*.000002
print(len(dt1))
print(x[len(x)-1]*timescale)

dt1=np.array(dt1,dtype=float)
title=args.title
fig, (figure)= plt.subplots(nrows=1, figsize=(8,5))
figure.scatter(x*timescale,dt1[0::100],color='black')
#plt.plot(x,log(x,*popt))
plt.ylim([0,8])
#plt.xticks(x)
plt.title(title)
plt.xlabel("ns")
plt.ylabel("nm")
plt.savefig("colvar-graphed.png")
