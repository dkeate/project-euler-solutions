# Smallest Multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
# remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



from collections import Counter
import tools.prime as prime

results_factors = []

for i in range(2, 21):
    result_counts = Counter(results_factors)
    merge_counts = Counter(prime.factors(i))

    missing = merge_counts - result_counts

    if missing:
        results_factors.extend(missing.elements())

        results_factors.sort()

results = 1

for p in results_factors:
    results = results * p

print(results)
