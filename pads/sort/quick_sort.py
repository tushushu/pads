# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:28:17
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:28:17
"""


def _partition_asc(nums, low, high):
    """Put the elements less than x on the left side 
    of the array, and the rest on the right side.

    Arguments:
        nums {list} -- 1d list with int or float.
        low {int} -- Left index.
        high {int} -- Right index.

    Returns:
        int -- The index of x.
    """

    i = low - 1
    for j in range(low, high):
        if nums[j] < nums[high]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def _partition_desc(nums, low, high):
    """Put the elements greater than x on the left side
    of the array, and the rest on the right side.

    Arguments:
        nums {list} -- 1d list with int or float.
        low {int} -- Left index.
        high {int} -- Right index.

    Returns:
        int -- The index of x.
    """

    i = low - 1
    for j in range(low, high):
        if nums[j] > nums[high]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def _quick_sort(nums, low, high, reverse):
    """Recursive quick sort.

    Arguments:
        nums {list} -- 1d list with int or float.
        low {int} -- Left index.
        high {int} -- Right index.
        reverse {bool} -- Descending sort or not.

    Returns:
        list -- List in order.
    """

    if low < high:
        if reverse:
            mid = _partition_desc(nums, low, high)
        else:
            mid = _partition_asc(nums, low, high)
        _quick_sort(nums, low, mid - 1, reverse)
        _quick_sort(nums, mid + 1, high, reverse)
    return nums


def quick_sort(nums, reverse=False):
    """Quick sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Keyword Arguments:
        reverse {bool} -- The default is ascending sort. (default: {False})

    Returns:
        list -- List in order.
    """

    low = 0
    high = len(nums) - 1
    return _quick_sort(nums, low, high, reverse)
