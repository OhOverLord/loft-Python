"""
Посчитайте размер матрицы Z в байтах и выведите его на печать.
Примечание. В этой задаче не нужно ничего считывать - матрица Z уже заполнена.
Sample Input 1:
np.zeros((10,10))
Sample Output 1:
800
Sample Input 2:
np.array([1,2,3], dtype=np.float64)
Sample Output 2:
24
"""

import numpy as np

Z = np.array([1, 2, 3], dtype=np.float64)
print(Z.itemsize * Z.size)