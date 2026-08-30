# Non-Abundant Sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the
# number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is
# called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
# all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
# upper limit cannot be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant
# numbers.



import tools.integer as integer

abundant = []

for i in range(12, 28124):
    factors = integer.factors(i)
    factors.remove(i)
    if sum(factors) > i:
        abundant.append(i)

sum_of_two = [False] * 28124

for i in range(len(abundant)):
    for j in range(i+1):
        if abundant[i] + abundant[j] < 28124:
            sum_of_two[abundant[i] + abundant[j]] = True
        else:
            break

results = []

for idx, is_sum in enumerate(sum_of_two):
    if not is_sum:
        results.append(idx)

print(sum(results))
