# Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
# into n). If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of
# a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71, and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.



import tools.integer as integer

results = []

for i in range(6, 10000):
    nums1 = integer.factors(i)
    nums1.remove(i)
    sum1 = sum(nums1)

    if sum1 <= 5 or sum1 == i:
        sum2 = -1
    else:
        nums2 = integer.factors(sum1)
        nums2.remove(sum1)
        sum2 = sum(nums2)

    if i == sum2:
        results.append(i)

print(sum(results))
