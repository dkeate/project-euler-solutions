# Largest Palindrome Product

# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit number is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.



def is_palindromic (n: int) -> bool:
    if str(n) == str(n)[::-1]:
        return True

    return False

largest = 0
for i in range(999, 0, -1):
    for j in range(999, i-1, -1):
        num = i * j
        if is_palindromic(num):
            if (num) > largest:
                largest = num

print(largest)
