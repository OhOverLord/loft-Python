"""
Считайте строку, где значения заданы через пробел shape и dtype
Последнее значение в строке может быть либо числом (тогда это последнее значение кортежа shape, либо строкой dtype)
Создайте матрицу Z размера shape, со значениями типа dtype (если dtype не указан, используйте numpy.float64)
Примечание. В этой задаче не нужно ничего выводить на печать. Только создать матрицу Z.
Sample Input 1:
5
Sample Output 1:
[0. 0. 0. 0. 0.]
Sample Input 2:
2 3 bool
Sample Output 2:
[[False False False]
 [False False False]]
"""

import numpy as np

s = input().split()
if s[-1].isdigit():
    s = [int(el) for el in s]
    Z = np.zeros(tuple(s))
else:
    t = s[-1]
    s = [int(el) for el in s[:-1]]
    Z = np.zeros(tuple(s), dtype=t)