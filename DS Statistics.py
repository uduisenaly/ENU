#1
import pandas as pd

full_health_data = pd.read_csv ("data.csv", header=10, sep=",")

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
print(full_health_data.describe())
#2
import pandas as pd
import numpy as np

full_health_data = pd.read_csv ("data.csv", header=0, sep=",")

Max_Pulse = full_health_data["Max_Pulse"]
percentile10 = np.percentile (Max_Pulse, 25)

print(percentile10)
#3
import pandas as pd
import numpy as np

full_health_data = pd.read_csv ("data.csv", header=0, sep=",")

cv = np.std(full_health_data)*np.mean(full_health_data)
print(cv)
#4
import pandas as pd
import numpy as np

health_data = pd.read_csv ("data.csv", header=0, sep=",")

var = np.var(health_data)

print(var)
