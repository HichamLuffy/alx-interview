#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    How many of this type of coin can I get with my money? Okay,
        I'll take that many. Now, how much money do I have left?
        And how many coins do I have in my pocket?
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1
