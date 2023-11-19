#1
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Calorie_Burnage', y='Max_Pulse', kind='line')
plt.ylim(ymin=130)
plt.xlim(xmin=60)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
#2
def slope(x1, y1, x2, y2):
  s = (y2-y1)/(x2-x1)
  return s

print(slope(50,150,70,200))
#3
def my_function(x):
  return 3*x + 66

print (my_function(125))
#4
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=190, ymax=350)
plt.xlim(xmin=50, xmax=180)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
