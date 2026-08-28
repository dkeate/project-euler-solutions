# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.

#    3*
#   7* 4
#  2 4* 6
# 8 5 9* 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route
# to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) 
# routes every second it would take over twenty billion years to check them all. There is an
# efficient algorithm to solve it. ;o)



triangle = []

with open('files/p0067_triangle.txt', 'r') as file:
    triangle = file.readlines()

nums = []

for line in triangle:
    nums.append([int(x) for x in line.split()])

result = []
result.append(nums[len(nums)-1])
result_line = 0

for i in range(len(nums) -2, -1, -1):
    line = []
    for pos, num in enumerate(nums[i]):
        entry = num

        if (result[result_line][pos] > result[result_line][pos+1]):
            entry = entry + result[result_line][pos]
        else:
            entry = entry + result[result_line][pos+1]

        line.append(entry)
    result.append(line)
    result_line = len(result) - 1

print(result[len(result)-1][0])
