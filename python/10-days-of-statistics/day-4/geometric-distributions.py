#### geometric distributions ####
# define functions
def factorial(x):
    """Calculates the factorial of the argument (an integer)"""
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans
    
def combination(x, n):
    """
    Returns the number of combinations of x values given n options.
    """
    return factorial(n)/(factorial(x)*factorial(n-x))
    
def neg_binomial(x, n, p):
    """
    Returns the probability of certain outcomes calculated from the negative binomial distribution for the given
    arguments:
    x = the number of successes
    n = the total number of trials
    p = the probability of success of one trial
    
    Note: when x = 1, we have what is called a geometric binomial.
    """
    return combination(x-1, n-1)*(p**x)*((1-p)**(n-x))

def cum_neg_binomial(x, n, p):
    """
    Returns the cumulative probability of a series of events calculated from the negative binomial distribution 
    for the given arguments:
    x = the number of successes
    n = the total number of trials
    p = the probability of success of one trial
    """
    # initialize integer to hold answer
    ans = 0
    for i in range(1, n+1):
        ans += neg_binomial(x, i, p)
    return ans

## Question #1
# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect 
# is found during the 5th inspection?
x = 1
n = 5
p = 1/3
print(round(neg_binomial(x, n, p), 3))

## Question #2
# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect 
# is found during the first 5 inspections?
x = 1
n = 5
p = 1/3
direction = "at most"
print(round(cum_neg_binomial(x, n, p), 3))
