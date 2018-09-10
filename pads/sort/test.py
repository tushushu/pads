# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-10 10:32:06
@Last Modified by:   tushushu
@Last Modified time: 2018-09-10 10:32:06
"""
from random import randint, choice
from time import time
from ..utils import duration_transfer


def correctness_test(fn, num_range=(-10, 10), len_range=(0, 10), n_tests=10000):
    """Test the correctness of sorting algorithm.

    Arguments:
        fn {function} -- Sorting algorithm.

    Keyword Arguments:
        num_range {tuple} -- The range of array elements. (default: {(-10, 10)})
        len_range {tuple} -- The range of array lenght. (default: {(0, 10)})
        n_tests {int} -- Number of tests. (default: {10000})
    """

    print("Testing correctness of %s for %d times!" % (fn.__name__, n_tests))
    for _ in range(n_tests):
        n = randint(*len_range)
        nums = [randint(*num_range) for _ in range(n)]
        reverse = choice([True, False])
        expected_ret = sorted(nums, reverse=reverse)
        actual_ret = fn(nums, reverse=reverse)
        error_str = "Test failed! Expected %s, but got %s" % (
            str(expected_ret), str(actual_ret))
        assert expected_ret == actual_ret, error_str
    print("Test passed!")


def efficiency_test(fn, num_range=(0, 1000), len_range=(100, 200), n_tests=1000):
    """Test the efficiency of sorting algorithm.

    Arguments:
        fn {function} -- Sorting algorithm.

    Keyword Arguments:
        num_range {tuple} -- The range of array elements. (default: {(0, 10000)})
        len_range {tuple} -- The range of array lenght. (default: {(0, 100)})
        n_tests {int} -- Number of tests. (default: {10000})
    """

    print("Testing efficiency of %s for %d times!" % (fn.__name__, n_tests))
    run_time = 0
    for _ in range(n_tests):
        n = randint(*len_range)
        nums = [randint(*num_range) for _ in range(n)]
        reverse = choice([True, False])
        start = time()
        fn(nums, reverse=reverse)
        run_time += time() - start
    ret = duration_transfer(run_time / n_tests)
    print("Average runtime %s!" % ret)
