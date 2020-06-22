"""
Имеется матрица Z
Добавьте вокруг имеющихся значений матрицы "забор" из 0.
Sample Input:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
Sample Output:
[[0 0 0 0 0]
 [0 1 2 3 0]
 [0 4 5 6 0]
 [0 7 8 9 0]
 [0 0 0 0 0]]
"""

import numpy as np


def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector


Z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Z = np.pad(Z, 1, pad_with)
