"""
Даны 2 вектора целых чисел A и B.
Найдите числа, встречающиеся в обоих векторах и составьте их по возрастанию в вектор Z.
Если пересечений нет, то вектор Z будет пустым.
Примечание. В этой задаче не нужно ничего выводить на печать. Только создать вектор Z.
Sample Input 1:
A = np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1])
B = np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])
Sample Output 1:
[1 3 7]
Sample Input 2:
A = np.arange(-5, 5)
B = np.array([9, -5, 2])
Sample Output 2:
[-5  2]
Sample Input 3:
A = np.array([1, 2, 3, 4, 5])
B = np.array([-5, -4, -3])
Sample Output 3:
[]
"""

import numpy as np

A = np.array([1, 2, 3, 4, 5])
B = np.array([-5, -4, -3])
Z = np.intersect1d(A, B)