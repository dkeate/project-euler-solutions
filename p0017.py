# Number Letter Counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
# letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
# 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when
# writing out numbers is in compliance with British usage.



nums = ["" for x in range(101)]

nums[1]   = "one"
nums[2]   = "two"
nums[3]   = "three"
nums[4]   = "four"
nums[5]   = "five"
nums[6]   = "six"
nums[7]   = "seven"
nums[8]   = "eight"
nums[9]   = "nine"
nums[10]  = "ten"
nums[11]  = "eleven"
nums[12]  = "twelve"
nums[13]  = "thirteen"
nums[14]  = "fourteen"
nums[15]  = "fifteen"
nums[16]  = "sixteen"
nums[17]  = "seventeen"
nums[18]  = "eighteen"
nums[19]  = "nineteen"
nums[20]  = "twenty"
nums[30]  = "thirty"
nums[40]  = "forty"
nums[50]  = "fifty"
nums[60]  = "sixty"
nums[70]  = "seventy"
nums[80]  = "eighty"
nums[90]  = "ninety"
nums[100] = "hundred"

results = []
results.append("")

for i in range(1, 1000):
    hundreds = i // 100
    tens = i % 100 // 10
    ones = i % 10
    next = ""

    if hundreds:
        next = nums[hundreds] + " hundred "
        if tens or ones:
            next = next + "and "

    if tens == 1:
        next = next + nums[(tens*10+ones)]
    else:
        next = next + nums[(tens*10)] + " " + nums[ones]

    results.append(next.strip())

results.append("one thousand")

count = 0

print(sum([len(x.replace(" ", "")) for x in results]))
