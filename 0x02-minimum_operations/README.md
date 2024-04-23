# Minimum Operations Function Explanation

The ``minOperations`` function is a Python function designed to solve the following problem:

Given a text file containing a single character `'H'`, you can perform only two operations: `Copy All` and `Paste`. The task is to find the minimum number of operations required to multiply the character 'H' to reach a specific count, denoted by ``n``.

## Algorithm Explanation

This function is based on the idea that the minimum number of operations needed to reach ``n`` 'H' characters is the sum of the prime factors of ``n``. The algorithm works as follows:

1. **Base Case**: If 'n' is less than or equal to 1, the function immediately returns 0 as no operations can be performed.

2. **Initialization**: The function initializes a counter for operations (`operations`) and a variable for the current factor (`factor`), starting at 2.

3. **Factorization Loop**: It proceeds to loop from this factor up to 'n', checking if 'n' is divisible by the current factor.

   - If 'n' is divisible by the current factor, it means we can perform a "Copy All" followed by `(factor - 1)` "Paste" operations, effectively duplicating the 'H' characters 'factor' times.
   - The function adds the value of `factor` to the `operations` count and divides `n` by `factor`.

4. **Loop Termination**: The loop continues until 'n' has been reduced to 1, meaning all factors have been accounted for.

5. **Return**: Finally, the function returns the `operations` count, representing the minimum number of operations needed.


- ## Function 
```py
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
```

- ## Usage

To use the `minOperations` function, you can import it into your Python script and pass an integer `n` as an argument. Here's an example:

```python
from minoperations import minOperations

n = 4
print(f"Min # of operations to reach {n} char: {minOperations(n)}")
```
