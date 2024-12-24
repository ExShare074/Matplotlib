# 2 Задача. Построить диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.

import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных чисел
random_arrray1 = np.random.rand(5)
random_arrray2 = np.random.rand(5)

# Построение диаграммы рассеяния
plt.scatter(random_arrray1, random_arrray2)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Диаграмма рассеяния')
plt.show()
