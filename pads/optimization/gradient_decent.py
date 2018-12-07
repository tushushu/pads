# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-03 18:05:25
@Last Modified by:   tushushu
@Last Modified time: 2018-12-03 18:05:25
"""
from random import random


def gradient_decent(fn, partial_derivatives, n_variables, lr=0.1,
                    max_iter=10000, tolerance=1e-5):
    theta = [random() for _ in range(n_variables)]
    y_cur = fn(*theta)
    for i in range(max_iter):
        # Calculate gradient of current theta.
        gradient = [f(*theta) for f in partial_derivatives]
        # Update the theta by the gradient.
        for j in range(n_variables):
            theta[j] -= gradient[j] * lr
        # Check if converged or not.
        y_cur, y_pre = fn(*theta), y_cur
        if abs(y_pre - y_cur) < tolerance:
            break
    return theta, y_cur
