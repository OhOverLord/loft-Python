"""
В Numpy можно предусмотреть различное поведение в случае ошибок (а не только то, что мы наблюдали в задаче 28).
Для этого используется функция https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.seterr.html
Отключите вывод всех ошибок (это довольно опасное поведение)
Sample Input:
Sample Output:
Кажется, я удачно поделил на 0 и не получил ошибок
"""

import numpy as np

np.seterr(all='ignore')