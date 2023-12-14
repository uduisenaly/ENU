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