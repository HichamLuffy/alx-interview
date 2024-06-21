#!/usr/bin/python3
"""
This module defines the function isWinner.
"""

def compute_primes(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    """Determine the winner of the game for x rounds given the list nums."""
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

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
