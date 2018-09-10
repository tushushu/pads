# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:29:22
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:29:22
"""


def merge(left, right):
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)
    res += left if left else right
    return res


def merge_sort(A):
    if len(A) <= 1:
        res = A
    else:
        mid = len(A) // 2
        left, right = merge_sort(A[:mid]), merge_sort(A[mid:])
        res = merge(left, right)
    return res
