# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:28:17
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:28:17
"""


def quick_sort(array):
    l, r = 0, len(array) - 1
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
