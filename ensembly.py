# Импорт необходимых библиотек
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загрузка набора данных о раке молочной железы
data = load_breast_cancer()
X = data.data  # Матрица признаков
y = data.target  # Целевые метки

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание модели случайного леса
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Обучение модели на обучающем наборе данных
rf_classifier.fit(X_train, y_train)

# Предсказание классов на тестовом наборе данных
y_pred = rf_classifier.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print("Точность модели случайного леса: {:.2f}".format(accuracy))