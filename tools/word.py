"""word.py

This module contains functions to analyze and manipulate words and letters.

Available functions:
    - permutations
    - permutations_of_length
"""


from typing import List

def permutations (elements: List[str]) -> List[str]:
    """Returns a list of all permutations of elements."""

    length = len(elements)

    if length == 0:
        raise ValueError("Elements must be non-empty.")

    if length != len(set(elements)):
        raise ValueError("Elements must all be unique.")

    for i in range(length):
        if len(elements[i]) != 1:
            raise ValueError("Permutation elements must be of length 1.")

    if length == 1:
        return elements

    # Heap's Algorithm: B. R. Heap (1963)
    count = [0] * length
    arr = elements.copy()
    results = ["".join(arr)]

    i = 1
    while i < length:
        if count[i] < i:
            if i % 2 == 0:
                arr[i], arr[0] = arr[0], arr[i]
            else:
                arr[count[i]], arr[i] = arr[i], arr[count[i]]

            results.append("".join(arr))
            count[i] += 1
            i = 0
        else:
            count[i] = 0
            i += 1

    return results

def permutations_of_length (elements: List[str], n: int) -> List[str]:
    """Returns a list of all permutations of elements of length n."""

    length = len(elements)

    if n <= 0:
        raise ValueError("Permutation length must be a positive integer.")

    if n > length:
        raise ValueError("Permutation length must be less than or equal to elements count.")

    if length != len(set(elements)):
        raise ValueError("Elements must all be unique.")

    for i in range(length):
        if len(elements[i]) != 1:
            raise ValueError("Permutation elements must be of length 1.")

    if length == 1:
        return elements

    # Algorithm 19 - Generating Combinations: Erwin Lee (1960)
    combos = []

    indices = list(range(n))

    combos.append([elements[i] for i in indices])

    while True:
        for i in reversed(range(n)):
            if indices[i] != i + length - n:
                break
        else:
            break

        indices[i] += 1

        for j in range(i + 1, n):
            indices[j] = indices[j-1] + 1

        combos.append([elements[i] for i in indices])

    results = []

    for combo in combos:
        results.extend(permutations(combo))

    return results
