# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:28:33
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:28:33
"""


def _bubble_sort_asc(nums):
    """Ascending bubble sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Returns:
        list -- List in ascending order.
    """

    n = len(nums)
    for i in range(1, n):
        for j in range(n - 1, i - 1,  -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def _bubble_sort_desc(nums):
    """Descending bubble sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Returns:
        list -- List in descending order.
    """

    n = len(nums)
    for i in range(1, n):
        for j in range(n - 1, i - 1,  -1):
            if nums[j] > nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def bubble_sort(nums, reverse=False):
    """Bubble sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Keyword Arguments:
        reverse {bool} -- The default is ascending sort. (default: {False})

    Returns:
        list -- List in order.
    """

    return _bubble_sort_desc(nums) if reverse else _bubble_sort_asc(nums)
