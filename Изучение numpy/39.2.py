"""
На вход подаются 3 числа (каждое с новой строки)
start
stop
n
Составьте список из n точек на отрезке [start, stop] в геометрической прогрессии, включая start и stop.
Округлите значения точек до 3 знака после запятой.
Результат сохраните в переменную Z.
Sample Input 1:
1
1000
4
Sample Output 1:
[   1.   10.  100. 1000.]
Sample Input 2:
1
256
9
Sample Output 2:
[  1.   2.   4.   8.  16.  32.  64. 128. 256.]
Sample Input 3:
1
100
5
Sample Output 3:
[  1.      3.162  10.     31.623 100.   ]
"""

import numpy as np

Z = np.around(np.geomspace(int(input()), int(input()), int(input()), endpoint=True), decimals=3)