#### quartiles ####

## define helper median function
def median(data):
    """Take in a list of integers and return the median value"""
    n = len(data)
    # if even number of integers
    if n%2 == 0:
        return (data[n//2]+data[n//2-1])/2
    # if odd number of integers
    else:
        return data[n//2]

## input and format data (originally string data)
# convert first line to integer
n = int(input())
# convert second line from space-separated string characters to sorted list of integers
data = sorted(list(map(int, input().split())))

## identify Q1, Q2, and Q3
# calculate median as average of middle values
q2 = int(median(data))
# create lower and upper halves depending on if even or odd number of elements
if n%2 == 0:
    l = data[:(n//2)]
    u = data[n//2:]    
else: 
    l = data[:(n//2)]
    u = data[(n//2+1):]
# calculate q1 and q3
q1 = int(median(l))
q3 = int(median(u))

## print results
print(q1)
print(q2)
print(q3)
