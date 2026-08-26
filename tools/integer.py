"""integer.py

This module contains functions to analyze and manipulate integers.

Available functions:
    - factors
"""

from typing import List
from math import sqrt

def factors (n: int) -> List[int]:
    "Returns a list of all factors of n."

    results = []

    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            results.append(i)
            results.append(n//i)

    results = list(set(results))
    results.sort()

    return results
