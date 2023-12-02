#1
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=1500)
plt.xlim(xmin=0, xmax=150)
plt.xlabel("Average_Pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
#2
import pandas as pd
import statsmodels.api as sm

# Загрузка данных из CSV-файла
full_health_data = pd.read_csv("data.csv", header=0, sep=",")

# Определение независимой и зависимой переменных
X = full_health_data["Average_Pulse"]  # Независимая переменная
y = full_health_data["Calorie_Burnage"]  # Зависимая переменная

# Добавление константы (intercept) к независимой переменной
X = sm.add_constant(X)

# Создание модели линейной регрессии
model = sm.OLS(y, X)

# Подгонка модели
results = model.fit()

# Вывод сводки результатов
print(results.summary())
#3
import pandas as pd
import statsmodels.formula.api as smf

# Загрузка данных из CSV-файла
full_health_data = pd.read_csv("data.csv", header=0, sep=",")

# Создание модели линейной регрессии с двумя независимыми переменными
model = smf.ols('Calorie_Burnage ~ Average_Pulse + Duration', data=full_health_data)

# Подгонка модели
results = model.fit()

# Вывод сводки результатов
print(results.summary())
