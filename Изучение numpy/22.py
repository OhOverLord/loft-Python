"""
"нормализовать" матрицу.
Sample Input 1:
1 2
2 1
Sample Output 1:
[[-1.  1.]
 [ 1. -1.]]
Sample Input 2:
99 11 55
33 66 99
Sample Output 2:
[[ 1.19 -1.54 -0.17]
 [-0.85  0.17  1.19]]
"""

import numpy as np

Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Z = (Y - np.mean(Y)) / (np.std(Y))
Z = np.around(Z, decimals=2)
print(Z)