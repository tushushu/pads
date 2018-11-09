# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-12 15:15:05
@Last Modified by:   tushushu
@Last Modified time: 2018-09-12 15:15:05
"""
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath(".."))


from pads.search.simulated_annealing import simulated_annealing
from math import sin, cos


def quadratic(x):
    """Quadratic function.

    Arguments:
        x {int}

    Returns:
        int
    """

    return x**2 - 2*x + 1


def absolute(x):
    return abs(x)


def main():
    functions = [sin, cos, quadratic, absolute]
    domains = [(-3.14, 3.14), (-3.14, 3.14), (-100, 100), (-10, 10)]
    optimizes = ["min", "max", "min", "min"]

    for f, domain, optimize in zip(functions, domains, optimizes):
        print("Solve the %simum value of %s function:" %
              (optimize, f.__name__))
        ret = simulated_annealing(
            fn=f, domain=domain, n_iter=10000, optimize=optimize)
        print("The solution is %.2f\n" % ret)


if __name__ == "__main__":
    main()
