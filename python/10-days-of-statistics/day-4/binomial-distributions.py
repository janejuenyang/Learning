#### binomial distribution, exercises #1 and #2 ####
# define functions
def factorial(x):
    """Calculates the factorial of the argument (an integer)"""
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans
    
def binomial(x, n, p):
    """
    Returns the probability of certain outcomes calculated from the binomial distribution for the given arguments:
    x = the number of successes
    n = the total number of trials
    p = the probability of success of one trial
    """
    return factorial(n)/(factorial(x)*factorial(n-x))*(p**x)*((1-p)**(n-x))    
    
def cum_binomial(x, n, p, direction):
    """
    Returns the cumulative probability of a series of events calculated from the binomial distribution for the given
    arguments:
    x = the number of successes
    n = the total number of trials
    p = the probability of success of one trial
    direction = "at least" or "at most"
    """
    # initialize integer to hold answer
    ans = 0
    # if direction is "at least"
    if direction == "at least":
        for i in range(x, n+1):
            ans += binomial(i, n, p)
    elif direction == "at most":
        for i in range(0, x+1):
            ans += binomial(i, n, p)
    else:
        print("Please indicate a direction of 'at least' or 'at most'.")
    return ans

## Question #1
# if the ratio of boys to girls for babies born in Russia is 1.09:1 and there is one child born per birth,
# what proportion of Russian families with exactly 6 children will have at least 3 boys?
x = 3 # three boys
n = 6 # six children
p = 1.09/(1+1.09) # proportion of boys in Russia
direction = "at least"

print(round(cum_binomial(x, n, p, direction), 3))

## Question #2
# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are 
# incorrectly sized. What is the probability that a batch of 10 pistons will contain:
# 1) at most 2 rejects?
# 2) at least 2 rejects?
x = 2 # number of rejects
n = 10 # number of engines in batch
p = 0.12 # proportion of rejects in engine batch

print(round(cum_binomial(x, n, p, direction = "at most"), 3))
print(round(cum_binomial(x, n, p, direction = "at least"), 3))
