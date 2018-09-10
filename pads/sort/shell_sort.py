# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:30:27
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:30:27
"""


def shell_sort(A):
    N = len(A)
    increment = N//2

    while increment > 0:
        i = increment

        while i < N:
            j = i - increment
            tmp = A[i]

            while j >= 0 and A[j] > tmp:
                A[j + increment] = A[j]
                j -= increment

            A[j + increment] = tmp
            i += 1

        increment //= 2

    return None


"""
test
"""

import random
import copy
import operator

k = 0
res = 0
t = 1000

while(k < t):
    A = [random.randint(-5, 5) for x in range(100)]
    B = copy.copy(A)

    shell_sort(A)
    B.sort()

    res += int(operator.eq(A, B))
    k += 1

if res == t:
    print("Pass!")
else:
    print("Wrong!")
