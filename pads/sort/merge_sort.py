# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-07 11:29:22
@Last Modified by:   tushushu
@Last Modified time: 2018-09-07 11:29:22
"""


def _merge_sort_asc(nums_left, nums_right):
    """Ascending merge sort.

    Arguments:
        nums_left {list} -- 1d list with int or float.
        nums_right {list} -- 1d list with int or float.

    Returns:
        list -- List in ascending order.
    """

    ret = []
    len_left = len(nums_left)
    len_right = len(nums_right)
    nums_left.append(float("inf"))
    nums_right.append(float("inf"))
    idx_left = idx_right = 0
    while idx_left < len_left or idx_right < len_right:
        if nums_left[idx_left] < nums_right[idx_right]:
            num = nums_left[idx_left]
            idx_left += 1
        else:
            num = nums_right[idx_right]
            idx_right += 1
        ret.append(num)
    return ret


def _merge_sort_desc(nums_left, nums_right):
    """Decending merge sort.

    Arguments:
        nums_left {list} -- 1d list with int or float.
        nums_right {list} -- 1d list with int or float.

    Returns:
        list -- List in decending order.
    """
    ret = []
    len_left = len(nums_left)
    len_right = len(nums_right)
    nums_left.append(-float("inf"))
    nums_right.append(-float("inf"))
    idx_left = idx_right = 0
    while idx_left < len_left or idx_right < len_right:
        if nums_left[idx_left] > nums_right[idx_right]:
            num = nums_left[idx_left]
            idx_left += 1
        else:
            num = nums_right[idx_right]
            idx_right += 1
        ret.append(num)
    return ret


def _merge_sort(nums, low, high, reverse):
    """Recursive merge sort.

    Arguments:
        nums {list} -- 1d list with int or float.
        low {int} -- Left index.
        high {int} -- Right index.
        reverse {bool} -- Descending sort or not.

    Returns:
        list -- List in order.
    """

    if high - low <= 1:
        ret = nums[low:high]

    else:
        mid = (low + high) // 2
        nums_left = _merge_sort(nums, low, mid, reverse)
        nums_right = _merge_sort(nums, mid, high, reverse)
        if reverse:
            ret = _merge_sort_desc(nums_left, nums_right)
        else:
            ret = _merge_sort_asc(nums_left, nums_right)
    return ret


def merge_sort(nums, reverse=False):
    """Merge sort.

    Arguments:
        nums {list} -- 1d list with int or float.

    Keyword Arguments:
        reverse {bool} -- The default is ascending sort. (default: {False})

    Returns:
        list -- List in order.
    """

    low = 0
    high = len(nums)
    return _merge_sort(nums, low, high, reverse)
