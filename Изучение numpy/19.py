"""
Считайте 2 числа: n, m.
Создайте матрицу размера n*m и "раскрасьте" её в шахматную раскраску.
0 - "чёрное"
1 - "белое"
Ячейка с координатами (0, 0) всегда "чёрная" (т.е. элемент (0, 0) равен 0).
Матрицу сохраните в переменную Z.
Примечание. В этой задаче не нужно ничего выводить на печать. Только создать матрицу Z.
Sample Input 1:
8 8
Sample Output 1:
<class 'numpy.ndarray'>
[[0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]
 [0. 1. 0. 1. 0. 1. 0. 1.]
 [1. 0. 1. 0. 1. 0. 1. 0.]]
Sample Input 2:
3 5
Sample Output 2:
<class 'numpy.ndarray'>
[[0. 1. 0. 1. 0.]
 [1. 0. 1. 0. 1.]
 [0. 1. 0. 1. 0.]]
"""

import numpy as np

n, m = map(int,input().split())
Z = np.zeros((n, m))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1