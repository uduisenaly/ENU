import math

class DataPoint:
    def __init__(self, x, y, class_name):
        self.X = x
        self.Y = y
        self.Class = class_name

def main():
    training_data = [
        DataPoint(2.0, 3.0, "Класс A"),
        DataPoint(3.0, 4.0, "Класс A"),
        DataPoint(5.0, 7.0, "Класс B"),
        DataPoint(7.0, 10.0, "Класс B")
    ]

    new_point = DataPoint(4.0, 5.0, "")

    k = 2

    predicted_class = classify(new_point, training_data, k)

    print(f"Предсказанный класс: {predicted_class}")

def classify(new_point, training_data, k):
    nearest_neighbors = sorted(training_data, key=lambda data: calculate_distance(new_point, data))[:k]

    class_counts = {}
    for neighbor in nearest_neighbors:
        if neighbor.Class in class_counts:
            class_counts[neighbor.Class] += 1
        else:
            class_counts[neighbor.Class] = 1

    return max(class_counts, key=class_counts.get)

def calculate_distance(point1, point2):
    delta_x = point1.X - point2.X
    delta_y = point1.Y - point2.Y
    return math.sqrt(delta_x * delta_x + delta_y * delta_y)

if __name__ == "__main__":
    main()
