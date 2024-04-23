#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        # If n is less than or equal to 1, it's not possible to perform operations.
        return 0
    
    operations = 0
    factor = 2
    
    while factor <= n:
        while n % factor == 0:
            # Increment the operations by the factor count
            operations += factor
            n //= factor
        factor += 1
    
    return operations
