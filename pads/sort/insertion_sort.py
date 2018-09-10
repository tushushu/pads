# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:25:03
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:25:03
"""


def insertion_sort(nums, reverse=False):
    """Insertion sort.

    Arguments:
        nums {list} -- 1d list with int.

    Keyword Arguments:
        reverse {bool} -- The default is ascending sort. (default: {False})

    Returns:
        list -- 1d list with int.
    """

    return _insertion_sort_desc(nums) if reverse else _insertion_sort_asc(nums)


def _insertion_sort_asc(nums):
    """Ascending insertion sort.

    Arguments:
        nums {list} -- 1d list with int.

    Returns:
        list -- List in ascending order.
    """
    
    n = len(nums)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                break
    return nums


def _insertion_sort_desc(nums):
    """Descending insertion sort.

    Arguments:
        nums {list} -- 1d list with int.

    Returns:
        list -- List in descending order.
    """

    n = len(nums)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                break
    return nums
