import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5) # массив из 5 случайных чисел
y = np.random.rand(5) # массив из 5 случайных чисел
print(x)
print(y)

plt.scatter(x, y)

plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("Тестовая диаграмма рассеяния")

plt.show()