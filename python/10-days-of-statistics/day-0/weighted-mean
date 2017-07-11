#### Weighted Means ####

## store input data
# number of values, converted to integer
n = int(input()) 
# numbers to calculated weighted mean of, converted to list of float
data = list(map(int, input().split()))
# weights, converted to list of ints
weights = list(map(int, input().split()))

## calculate the weighted mean
# initialize a new list for the sumproduct of the numbers and weights
weighted_data = []
for i in range(len(data)):
    weighted_data.append(data[i] * weights[i])
# sum weighted_data list and divide by the sum of the weights
print(round(sum(weighted_data)/sum(weights), 1))
