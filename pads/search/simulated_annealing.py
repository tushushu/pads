# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-11 15:01:23
@Last Modified by:   tushushu
@Last Modified time: 2018-09-11 15:01:23
"""
from random import random, randint, uniform
from math import exp, log


def schedule(t, alpha, init_temp, method):
    """Temperature schedule.

    Arguments:
        k {int} -- Time of annealing process.
        alpha {float} -- The exponential decay argument.
        init_temp {float} -- Initial temperature.
        method {str} -- Temperature schedule method.

    Returns:
        float -- Temperature.
    """

    assert method in ('exp', 'log'), "Parameter method must in ('exp', 'log')!"
    # Fast
    if method == "exp":
        return init_temp * (alpha ** t)
    # Slow
    if method == "log":
        return init_temp / log(1 + alpha * t)


def simulated_annealing(fn, domain, n_iter, min_temp=1e-10, optimize="min", alpha=0.95, init_temp=1e4, method='exp'):
    """The simulated annealing algorithm.

    Arguments:
        fn {function} -- Function of problem to solve.
        domain {tuple} -- The domain of the independent variable.
        n_iter {int} -- Number of iterations in a temperature.


    Keyword Arguments:
        min_temp {float} -- The minimum temperature. (default: {1e-10})
        optimize {str} -- To get the maximum or minimum solution. (default: {"min"})
        alpha {float} -- The exponential decay argument. (default: {0.95})
        init_temp {float} -- Initial temperature. (default: {1e4})
        method {str} -- Temperature schedule method. (default: {'exp'})

    Returns:
        float -- An approximate solution.
    """

    assert optimize in (
        "min", "max"), "Argument optimize must be 'min' or 'max'!"
    flag = {"min": -1, "max": 1}[optimize]
    # Time
    t = 1
    # Initial temperature.
    temp = schedule(t, alpha, init_temp, method)
    # Initial solution.
    x_min, x_max = domain
    x = uniform(x_min, x_max)
    while temp >= min_temp:
        for _ in range(n_iter):
            # Choose a new solution randomly.
            x_new = x + uniform(-1, 1) * temp
            # If x is in the domain.
            if x_new > x_max or x_new < x_min:
                continue
            delta = (fn(x_new) - fn(x)) * flag
            # The local optimal solution is skipped by a certain probability.
            if delta > 0:
                x = x_new
            else:
                prob = exp(delta / temp)
                if prob > random():
                    x = x_new
        t += 1
        temp = schedule(t, alpha, init_temp, method)
    return x
