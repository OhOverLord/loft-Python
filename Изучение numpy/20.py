"""
Даны:
индекс i
numpy массив Z
Определите "координаты" элемента с индексом i в Z и выведите кортеж с координатами на печать.
Примечание. В этой задаче не нужно ничего считывать. i и Z уже заполнены.
Sample Input 1:
i = 5
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
Sample Output 1:
(1, 1)
Sample Input 2:
i = 3
array([ 10,  11,  12,  13,  14,  15])
Sample Output 2:
(3,)
Sample Input 3:
i = 4
array([[[ 1,  2],
        [ 3,  4]],

       [[11, 12],
        [13, 14]]])
Sample Output 3:
(1, 0, 0)
"""

import numpy as np

i = 5
Z = np.array([[[1,  2], [3,  4]], [[11, 12], [13, 14]]])
print(np.unravel_index(i, Z.shape))