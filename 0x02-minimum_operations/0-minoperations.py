#!/usr/bin/python3
"""
Minimum operatieons
"""


def minOperations(n):
    """

    :parametre n:
    :return:
    """
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
