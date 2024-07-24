#!/usr/bin/python3
"""
Interview question task
"""


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed
    to meet a given amount total.

    Args:
        coins: is a list of the values of the coins in your possession
        total: Total to determine

    Returns:
        Total number of coins
    """
    if (total <= 0):
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
