# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-07 11:33:03
@Last Modified by:   tushushu
@Last Modified time: 2018-12-07 11:33:03
"""
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath(".."))


from pads.optimization.gradient_decent import gradient_decent


def f(x, y):
    return (x + y - 3) ** 2 + (x + 2 * y - 5) ** 2 + 2


def df_dx(x, y):
    return 2 * (x + y - 3) + 2 * (x + 2 * y - 5)


def df_dy(x, y):
    return 2 * (x + y - 3) + 4 * (x + 2 * y - 5)


def main():
    print("Solving the minimum value of quadratic function:")
    n_variables = 2
    theta, f_theta = gradient_decent(f, [df_dx, df_dy], n_variables)
    theta = [round(x, 3) for x in theta]
    print("The solution is: theta %s, f(theta) %.2f.\n" % (theta, f_theta))


if __name__ == "__main__":
    main()
