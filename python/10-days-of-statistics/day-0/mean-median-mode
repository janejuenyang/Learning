#### Day 0: Mean, Median, and Mode ####

# Note: I am intentionally not using existing Python modules to simplify this code, because I want to practice the concept
#       more than the code

## format input data
# read first line and convert into integer format
n = int(input())
# read second line, split into a list, convert each element into floats, and sort
data = sorted(list(map(int, input().split())))

## calculate the mean
mean = sum(data)/n
print(round(mean), 1)

## calculate the median
# if an even number of inputs, take the mean of the middle two indices
# else, since it's an odd number of inputs, just select the middle index
if n%2 == 0:
    median = (data[n//2] + data[n//2 - 1])/2
else:
    median = data[n//2]
print(round(median), 1)

## calculate the mode
# create a dictionary with each unique number in the list and the count of each number
data_dict = dict((x, data.count(x)) for x in set(data))
# identify the maximum number of times a value is listed
max_count = max(data_dict.values())
# print the smallest key that is associated with the maximum value
subdata_dict = {key: data_dict[key] for key in data_dict if data_dict[key] == max_count}
print(min(subdata_dict))
