# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:30:27
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:30:27
"""


def shell_sort(nums, reverse):
    """Shell sort.

    Arguments:
        nums {list} -- 1d list with int.

    Keyword Arguments:
        reverse {bool} -- The default is ascending sort. (default: {False})

    Returns:
        list -- 1d list with int.
    """
    return _shell_sort_desc(nums) if reverse else _shell_sort_asc(nums)


def _shell_sort_asc(nums):
    """Ascending shell sort.

    Arguments:
        nums {list} -- 1d list with int.

    Returns:
        list -- List in ascending order.
    """

    n = len(nums)
    increment = n // 2
    while increment > 0:
        for i in range(increment, n):
            for j in range(i - increment, -1, -increment):
                if nums[j] > nums[j + increment]:
                    nums[j], nums[j + increment] = nums[j + increment], nums[j]
                else:
                    break
        increment = increment // 2
    return nums


def _shell_sort_desc(nums):
    """Descending shell sort.

    Arguments:
        nums {list} -- 1d list with int.

    Returns:
        list -- List in descending order.
    """

    n = len(nums)
    increment = n // 2
    while increment > 0:
        for i in range(increment, n):
            for j in range(i - increment, -1, -increment):
                if nums[j] < nums[j + increment]:
                    nums[j], nums[j + increment] = nums[j + increment], nums[j]
                else:
                    break
        increment = increment // 2
    return nums
