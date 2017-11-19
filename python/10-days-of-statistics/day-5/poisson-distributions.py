#### poisson distributions ####

## define functions
def factorial(x):
    """Calculates the factorial of the argument (an integer)"""
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans

def poisson(l, k):
    """
    Returns the Poisson probability of k success occuring given an average lambda (l) number of successes in the same period.
    """
    # in base python, we truncate the value of e
    # in an actual analysis, import math module instead and use exp() function
    e = 2.71828
    return (l**k * e**-l)/factorial(k)

## input and format data (originally string data)
# convert first line to float numeric
l = float(input())
# convert second line to integer
k = int(input())

## calculate and print answer
print(round(float(poisson(l, k)), 3))
