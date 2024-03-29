"""
Считайте 3 числа: n, m, l.
Зафиксируйте значение генератора случайных чисел Numpy с помощью
numpy.random.seed(42)
Создайте матрицу n*m*l из случайных чисел (от 0 до 1) и сохраните результат в переменную Z.
Примечание. В этой задаче не нужно ничего выводить на печать. Только создать матрицу Z.
Sample Input:
2 2 2
Sample Output:
[[[0.37454012 0.95071431]
  [0.73199394 0.59865848]]

 [[0.15601864 0.15599452]
  [0.05808361 0.86617615]]]
"""

import numpy as np

n, m, l = map(int, input().split())
np.random.seed(42)
Z = np.random.random((n, m, l))