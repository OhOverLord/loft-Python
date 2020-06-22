"""
Дан вектор Z
Запишите в переменную NonZerros индексы ненулевых элементов.
Используйте функцию https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.nonzero.html
Примечание. В этой задаче не нужно ничего считывать или выводить на печать. Матрица ﻿Z уже готова, просто создайте ﻿NonZerros﻿.
Sample Input 1:
array([1, 0, 2, 0, 3, 0, 4])
Sample Output 1:
(array([0, 2, 4, 6]),)
Sample Input 2:
[1, 2, 0, 0, 4, 0]
Sample Output 2:
(array([0, 1, 4]),)
"""


import numpy as np

Z = np.array([1, 0, 2, 0, 3, 0, 4])
NonZerros = np.nonzero(Z)