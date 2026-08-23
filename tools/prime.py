"""prime.py

This module contains functions to generate and identify primes.

Available functions:
    - generate
    - generate_below
    - is_prime
    - factors
"""

from typing import List
from math import log, sqrt

def generate (n: int) -> List[int]:
    """Returns a list of the first n primes."""

    if n < 1:
        return []

    # Dusart's Shifted Upper Bound: Dusart (1999)
    if n < 6:
        upper_bound = 11.0
    else:
        upper_bound = n * (log(n) + log(log(n)))
        
    print(upper_bound)

    result = generate_below(int(upper_bound)+1)
    result = result[:n]

    return result

def generate_below (limit: int) -> List[int]:
    """Returns a list of primes that are below limit."""

    # Sieve of Eratosthenes: Eratosthenes of Cyrene (240 BCE)
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime [i] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def is_prime (n: int) -> bool:
    """Returns True if a number is a prime positive int. Otherwise, returns False."""

    if n <= 1: return False
    if n <= 3: return True

    # Optimized Trial Division: Selfridge and Wunderlich (1974)
    if n % 2 == 0 or n % 3 == 0: return False

    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def factors (n: int) -> List[int]:
    """Returns list of prime factors."""

    if n < 2:
        raise ValueError("Prime numbers must be higher than 1.")

    results = []

    # Optimized Trial Division: Selfridge and Wunderlich (1974)
    while n % 2 == 0:
        results.append(2)
        n = n // 2

    while n % 3 == 0:
        results.append(3)
        n = n // 3

    found = False

    while not found:
        for i in range(5, int(sqrt(n)) + 1, 6):
            if n % i == 0:
                results.append(i)
                n = n // i
                break
            if n % (i + 2) == 0:
                results.append(i + 2)
                n = n // (i + 2)
                break
        else:
            found = True

    if (n != 1):
        results.append(n)

    return results
