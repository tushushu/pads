# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-10 22:23:11
@Last Modified by:   tushushu
@Last Modified time: 2018-09-10 22:23:11
"""


def _select_sort_asc(nums):
    """Ascending select sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Returns:
        list -- List in ascending order.
    """

    n = len(nums)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[idx]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums


def _select_sort_desc(nums):
    """Descending select sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Returns:
        list -- List in descending order.
    """

    n = len(nums)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if nums[j] > nums[idx]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums


def select_sort(nums, reverse=False):
    """Select sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Keyword Arguments:
        reverse {bool} -- The default is ascending sort. (default: {False})

    Returns:
        list -- List in order.
    """

    return _select_sort_desc(nums) if reverse else _select_sort_asc(nums)
