#### standard deviation ####

## define helper functions
def mean(source):
    """Calculates the arithmetic mean from a list of integers or floats"""
    return sum(source)/len(source)

def sq_dist_to_mean(source, mean):
    """Takes in a list of integers or floats and a mean value to calculate the total squared distance from the mean"""
    answer = 0
    for i in source:
        answer += (i - mean)**2
    return(answer)

def sd(source):
    """Calculates the standard deviation from a list of integers or floats"""
    n = len(source)
    return((sq_dist_to_mean(source, mean(source))/n)**0.5)

## gather and format input data
n = int(input())
data = list(map(int, input().split()))

print(round(sd(data), 1))
