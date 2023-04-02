# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/21  021 上午 9:30
@Author  : Jan
@File    : 质数(素数)判断.py
"""

""" {} """


def is_prime1(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_prime2(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def is_prime3(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def is_prime4(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True
