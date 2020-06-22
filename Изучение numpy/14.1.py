"""
Считайте 2 числа: n, m.
Зафиксируйте значение генератора случайных чисел Numpy с помощью
numpy.random.seed(42)
Создайте матрицу n*m из случайных чисел (от 0 до 1).
Найдите среднее значение для каждого из столбцов.
Выведите на печать значение минимального и максимального среднего по столбцам (каждое с новой строки).
Sample Input 1:
3 4
Sample Output 1:
0.270220682758469
0.8115814940446553
Sample Input 2:
12 6
Sample Output 2:
0.3978200241403143
0.5425150112777877
"""

import numpy as np

n, m = map(int, input().split())
np.random.seed(42)
Z = np.random.random((n, m))
print(min(Z.mean(axis=0)))
print(max(Z.mean(axis=0)))