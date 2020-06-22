"""
Дана матрица чисел Z (Z может быть 1, 2 или даже 3 мерной).
Выведите на печать список чисел из этой матрицы, которые больше 3.
Sample Input 1:
np.array([1, 2, 3, 4])
Sample Output 1:
[4]
Sample Input 2:
np.array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [0, 0, 9]])
Sample Output 2:
[4, 5, 6, 7, 8, 9, 9]
Sample Input 3:
np.array([[[1, 2],
           [4, 5]],
          [[7, 8],
           [0, 0]]])
Sample Output 3:
[4, 5, 7, 8]
"""

import numpy as np

Z = np.array([[[1, 2], [4, 5]], [[7, 8], [0, 0]]])
print(list(Z[Z > 3]))