#### poisson distribution applied in a factory setting ####

## define functions
def expectedX2(l):
    """
    Given a Poisson random variable (X) with mean lambda (l), return the expected squared value (X^2)
    Given for a Poisson distbirution:
        E[X] = l
        Var(X) = l
    Solve for X^2:
        Var(X) = E[X^2] - (E[X])^2
        E[X^2] = Var(X) + (E[X])^2
        E[X^2] = l + l^2
    """
    return l + l**2

def dailyCostA(l):
    """
    Returns the expected daily operating cost for 'Machine A' given a number of repairs needed, k,
    which is a Poisson random variable.
    """
    return 160 + 40 * expectedX2(l)

def dailyCostB(l):
    """
    Returns the expected daily operating cost for 'Machine A' given a number of repairs needed, k,
    which is a Poisson random variable.
    """
    return 128 + 40 * expectedX2(l)


## input the lambda values for Machines A and B, converting from a space-separated string into list of floats
lambdas = list(map(float, input().split()))

## calculate and print answers
# expected daily cost of machine A
print(round(float(dailyCostA(lambdas[0])), 3))

# expected daily cost of machine B
print(round(float(dailyCostB(lambdas[1])), 3))
