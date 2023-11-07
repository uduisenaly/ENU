import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb

# Загрузка данных
data = pd.read_csv('airport_data.csv')

# Подготовка данных
data['is_north'] = (data['latitude'] > 50).astype(int)
X = data[['latitude', 'other_features']]
y = data['is_north']

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели XGBoost
model = xgb.XGBClassifier(n_estimators=100, max_depth=3)
model.fit(X_train, y_train)

# Оценка модели
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy}')

# Прогнозирование
new_data = pd.DataFrame({'latitude': [51.2, 47.1], 'other_features': [values]})
predictions = model.predict(new_data)
print(predictions)
