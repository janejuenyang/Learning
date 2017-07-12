#### interquartile range ####

## define helper functions
def expand(elements, frequency):
    """
    Take in two lists of strings: one of elements, and one of frequency of each element
    Return a single expanded and sorted list of integer elements based on the designated frequency
    """
    # first create a list of the expanded lists
    output = []
    for i in range(len(elements)):
        output.append([elements[i]]*frequency[i])
    # flatten into a single list
    output = [element for sublist in output for element in sublist]
    # convert elements to integers and sort
    output = sorted(map(int, output))
    return output

def median(data):
    """Take in a list of integers and return the median value"""
    n = len(data)
    # if even number of integers
    if n%2 == 0:
        return (data[n//2]+data[n//2-1])/2
    # if odd number of integers
    else:
        return data[n//2]

def iqr(data):
    """Calculates the interquartile range from a list of integers or floats"""
    # define length of list
    n = len(data)

    ## identify Q1 and Q3
    # create lower and upper halves depending on if even or odd number of elements
    if n%2 == 0:
        l = data[:(n//2)]
        u = data[n//2:]    
    else: 
        l = data[:(n//2)]
        u = data[(n//2+1):]
    # calculate q1 and q3
    q1 = median(l)
    q3 = median(u)
    # return the interquartile range
    return q3 - q1

## input and format data (originally string data)
# convert first line to integer; we won't be using this input though
n = int(input())
# convert second and third lines from space-separated strings to a list of strings and integers respectively
elements = input().split()
freq = list(map(int, input().split()))
# convert elements and freq into a single, expanded list
data = expand(elements, freq)

## calculate and print interquartile range for expanded data
print(round(float(iqr(data)), 1))
