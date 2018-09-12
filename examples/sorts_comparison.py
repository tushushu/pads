# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-10 13:50:04
@Last Modified by:   tushushu
@Last Modified time: 2018-09-10 13:50:04
"""
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath(".."))

from pads.sort.test import correctness_test, efficiency_test
from pads.sort.bubble_sort import bubble_sort
from pads.sort.insertion_sort import insertion_sort
from pads.sort.shell_sort import shell_sort
from pads.sort.merge_sort import merge_sort
from pads.sort.quick_sort import quick_sort
from pads.sort.select_sort import select_sort


def main():
    for test_fn in [correctness_test, efficiency_test]:
        print(test_fn.__name__)
        for sort_fn in [select_sort, bubble_sort, insertion_sort, shell_sort, merge_sort, quick_sort]:
            test_fn(sort_fn)
            print()


if __name__ == "__main__":
    main()
