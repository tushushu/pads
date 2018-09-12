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


if __name__ == "__main__":
    print("Solve the minimum value of Sin function:")
    print(simulated_annealing(sin, (-3.14, 3.14), 1000))
    print()
    print("Solve the minimum value of Cos function:")
    print(simulated_annealing(cos, (-3.14, 3.14), 1000, optimize="max"))
