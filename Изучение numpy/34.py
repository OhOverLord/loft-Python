"""
1-я входная строка - год (опционально месяц и день) в формате ISO начала отсчёта
2-я входная строка - год (опционально месяц и день) в формате ISO окончания отсчёта
Составьте список (numpy array) дат с шагом в 1 день от начала до окончания отсчёта (последний день не включается).
Результат должен представлять из себя список дат в формате ISO.
Пример - 2005-02-25, где
2005 - год
02 - месяц
25 - день
Запишите результат в переменную Z
Sample Input 1:
2016-07
2016-08
Все даты в июле 2016
Sample Output 1:
['2016-07-01' '2016-07-02' '2016-07-03' '2016-07-04' '2016-07-05'
 '2016-07-06' '2016-07-07' '2016-07-08' '2016-07-09' '2016-07-10'
 '2016-07-11' '2016-07-12' '2016-07-13' '2016-07-14' '2016-07-15'
 '2016-07-16' '2016-07-17' '2016-07-18' '2016-07-19' '2016-07-20'
 '2016-07-21' '2016-07-22' '2016-07-23' '2016-07-24' '2016-07-25'
 '2016-07-26' '2016-07-27' '2016-07-28' '2016-07-29' '2016-07-30'
 '2016-07-31']
Sample Input 2:
2019-02-22
2019-03
Sample Output 2:
['2019-02-22' '2019-02-23' '2019-02-24' '2019-02-25' '2019-02-26'
 '2019-02-27' '2019-02-28']
Sample Input 3:
2019
2019-01-09
Новогодние каникулы в 2019
Sample Output 3:
['2019-01-01' '2019-01-02' '2019-01-03' '2019-01-04' '2019-01-05'
 '2019-01-06' '2019-01-07' '2019-01-08']
"""

import numpy as np

Z = np.arange(input(), input(), dtype='datetime64[D]')