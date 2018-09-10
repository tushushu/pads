# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-09-10 14:31:33
@Last Modified by:   tushushu
@Last Modified time: 2018-09-10 14:31:33
"""


def duration_transfer(duration):
    """Transfer the time duration's unit to a proper one.

    Arguments:
        duration {float} -- Time duration.

    Returns:
        str -- with "ns", "us", "ms" or "s"
    """

    if duration < 1e-6:
        unit = "ns"
        duration *= 1e9
    elif duration < 1e-3:
        unit = "us"
        duration *= 1e6
    elif duration < 1:
        unit = "ms"
        duration *= 1e3
    else:
        unit = "s"
    return "%.3f %s" % (duration, unit)
