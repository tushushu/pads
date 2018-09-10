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


def main():
    correctness_test(bubble_sort)
    efficiency_test(bubble_sort)


if __name__ == "__main__":
    main()
