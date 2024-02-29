#!/usr/bin/python3

def makeChange(coins, total):
    """make change function to get the smallest
    number of coins to get to a total

    Args:
        coins (list): the coins to combine
        total (int): the total to reach

    Returns:
        int: the count of coins
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    current_sum = []
    for i in range(len(coins)):
        while sum(current_sum) + coins[i] <= total:
            current_sum.append(coins[i])
        i += 1
    if sum(current_sum) == total:
        return len(current_sum)
    else:
        return -1
