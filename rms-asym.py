import numpy as np
import pandas as pd
import argparse
from scipy.optimize import curve_fit
import matplotlib
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-i')
args = parser.parse_args()

data=pd.read_csv(args.i,header=18,delimiter='   ',engine='python')
time,rms=[],[]
for i in data.values:
    time.append(i[0])
    rms.append(i[1])
time=np.array(time)
rms=np.array(rms)

def func(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
def func2(x,a,b,c):
    return a*np.exp(-b*x) + c
rms=rms-np.mean(rms)
popt,pcov = curve_fit(func2, time, rms)
print(popt)
plt.plot(time,rms)
plt.plot(time,func2(time,*popt))
plt.show()
