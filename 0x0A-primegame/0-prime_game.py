#!/usr/bin/python3
"""This module defines the function isWinner."""


def compute_primes(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes
    this function return an array of prime numbers
    smaller or equal to n using Sieve of Eratosthenes"""
    result = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            result.append(p)
    return result


def isWinner(x, nums):
    """Determine the winner of the
    game for x rounds given the list nums."""
    if x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = compute_primes(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
