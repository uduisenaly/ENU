import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = load_boston()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

tree_reg = DecisionTreeRegressor()
tree_reg.fit(X_train, y_train)

y_pred_lin = lin_reg.predict(X_test)
y_pred_tree = tree_reg.predict(X_test)

y_pred_combined = (y_pred_lin + y_pred_tree) / 2

mse_lin = mean_squared_error(y_test, y_pred_lin)
mse_tree = mean_squared_error(y_test, y_pred_tree)
mse_combined = mean_squared_error(y_test, y_pred_combined)

print("MSE - Linear Regression:", mse_lin)
print("MSE - Decision Tree:", mse_tree)
print("MSE - Combined Model:", mse_combined)
