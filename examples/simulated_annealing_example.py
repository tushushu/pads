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
    return x**2 - 2 * x + 1


def main():
    functions = [sin, cos, quadratic]
    domains = [(-3.14, 3.14), (-3.14, 3.14), (-100, 100)]
    optimizes = ["min", "max", "min"]

    for f,  domain, optimize in zip(functions, domains, optimizes):
        print("Solve the minimum value of %s function:" % f.__name__)
        ret = simulated_annealing(
            fn=f, domain=domain, n_iter=1000, optimize=optimize)
        print("The result is %.2f\n" % ret)


if __name__ == "__main__":
    main()
