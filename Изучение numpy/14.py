"""
Считайте 2 числа: n, m.
Зафиксируйте значение генератора случайных чисел Numpy с помощью
numpy.random.seed(42)
Создайте матрицу n*m из случайных чисел (от 0 до 1).
Выведите на печать значение среднего для всей матрицы.
Sample Input 1:
30 30
Sample Output 1:
0.4923750160905882
Sample Input 2:
12 6
Sample Output 2:
0.46798212705144554
"""

import numpy as np

n, m = map(int, input().split())
np.random.seed(42)
Z = np.random.random((n, m))
print(Z.mean())