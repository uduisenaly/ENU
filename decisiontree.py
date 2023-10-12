# Импорт необходимых библиотек
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загрузка набора данных Iris
iris = load_iris()
X = iris.data  # Матрица признаков
y = iris.target  # Целевые метки

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание модели решающего дерева
classifier = DecisionTreeClassifier(random_state=42)

# Обучение модели на обучающем наборе данных
classifier.fit(X_train, y_train)

# Предсказание классов на тестовом наборе данных
y_pred = classifier.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print("Точность модели: {:.2f}".format(accuracy))