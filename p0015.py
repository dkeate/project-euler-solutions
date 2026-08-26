# Lattice Paths

# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and
# down, there are exactly 6 routes to the bottom right corner.

# Photo at: https://projecteuler.net/problem=15

# How many such routes are there through a 20 x 20 grid?



from functools import cache

@cache
def solve (x, y):
    if x and y:
        return solve(x-1, y) + solve(x, y-1)
    elif x:
        return solve(x-1, y)
    elif y:
        return solve(x, y-1)
    else:
        return 1

print(solve (20, 20))
