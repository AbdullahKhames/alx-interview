#!/usr/bin/python3
"""module to calculate min operations needed for
a letter to reach a given n repetitions
"""


def minOperations(n):
    """function to calculate min operations
        counter += 1 represents the copy all
        sum += step represents the paste
    Args:
        n (int): the end wanted number of copies of single char
    return: the counter of operations
    """
    counter = 0
    sum = 1
    step = 1
    if n < 1:
        return 0
    if n == 2:
        return 2
    while sum != n:
        step, counter = calculate_step(n, sum , step, counter)
        sum += step
        counter += 1
    return counter


def calculate_step(n, sum, step, counter):
    """function that returns step val

    Args:
        n (int): the final wanted number
        sum (int): the current sum
        step (int): the current step
    """
    # step_div = n / step
    # step_mod = n % step
    # sum_div = n / sum
    sum_mod = n % sum
    if sum_mod == 0:
        counter += 1
        return sum, counter
    return step, counter
