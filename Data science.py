#1
pulse_min = min (52,75,6,33,189,527,96,12,873)
print(pulse_min)
#2
pulse_max = max (52,75,6,33,189,527,96,12,873)
print(pulse_max)
#3
import numpy as np 
Calorie_burnage = [52,75,6,33,189,527,96,12,873]
Average_calorie_burnage = np.mean (Calorie_burnage)
print (Average_calorie_burnage)
#4
import pandas as pd 
d = {'New_Column_1': [10,20,30,40,70], 'New_Column_1': [40,50,60,90,50],
'New_Column_3': [70,80,120,10,110]}
df = pd.DataFrame (dta = d)
print (df)
#5
Array = [3,896,86,73,19,75,765,7815,17,435,52,963]
print (Array)
#6
import sys
import matplotlib
matplotlib.use ('Agg')

import pandas aas pdimport matplotlib.pyplot as pyplotfrom scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x=full_health_data["Average_pulse"]
x=full_health_data["Calorie_Burnage"]

slope, intercept,r,p,std_err = stats.linregress(x,y)

def myfuns (x):
return slope * x + intercept
mymodel = list(map(myfunc,x))

plt.scatter (x,y)
plt.plot (x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=2000)
plt.xlabel ("Average_pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()
