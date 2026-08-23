# Largest Prime Factor

# The prime factors of 13195 are 5, 7, 13, and 29.

# What is the largest prime factor of the number 600851475143?



from math import sqrt
import tools.prime as prime

num = 600851475143

for p in prime.generate_below (int(sqrt(num))):
    if num % p == 0:
        num = num//p
        if prime.is_prime(num):
            break

print(num)
