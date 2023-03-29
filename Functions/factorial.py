# 5 factorial
# Create a function called `calculateFactorial()`
#  that returns the factorial of its input




def calculatefactorial(n):
    if n == 0:
        return 1
    else:
        return n * calculatefactorial(n-1)
n=int(input("Input a number to calculate the factiorial : "))
print(calculatefactorial(n))
