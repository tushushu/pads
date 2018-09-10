# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:25:03
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:25:03
"""


def insertion_sort(nums):
    l = len(nums)
    for i in range(1, l):
        key = nums[i]
        j = i-1
        while nums[j] > key and j >= 0:
            nums[j+1] = nums[j]
            nums[j] = key
            j = j-1
    return nums
