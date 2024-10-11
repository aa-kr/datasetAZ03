import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
print(data)
plt.hist(data, bins=10)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")
plt.show()