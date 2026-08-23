"""fibonacci.py

This module calculates Fibonacci sequences under different contstraints.

Available functions:
    - generate
    - generate_below
"""

from typing import List

def generate (n: int) -> List[int]:
    """Returns a list of the first n values in the Fibonacci sequence."""

    if n <= 2:
        raise ValueError("Fibonacci sequence must contain at least 3 values.")

    result = [1,2]
    a=1
    b=2

    for i in range(n-2):
        c=a+b
        result.append(c)
        a=b
        b=c
        
    return result



def generate_below (limit: int) -> List[int]:
    """Returns a list of values in the Fibonacci sequence that are below limit."""

    if limit <= 2:
        raise ValueError("Fibonacci sequence must contain at least 3 values.")

    result = [1,2]
    a=1
    b=2
    c=3

    while c < limit:
        result.append(c)

        a=b
        b=c
        c=a+b

    return result
