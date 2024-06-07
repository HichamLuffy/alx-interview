#!/usr/bin/python3
""" making change """


def makeChange(coins, total):
    """makechange"""
    if total <= 0:
        return 0

    # Initialize dp array with a large value (total + 1)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Update dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1

