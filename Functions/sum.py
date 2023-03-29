# 4 sum
# Write a function called `sum()` that returns the sum of numbers from zero to the given parameter


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


