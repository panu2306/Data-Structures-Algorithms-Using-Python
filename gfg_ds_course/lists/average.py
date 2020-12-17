def simple_average(l):
    sum = average = length = 0
    length = len(l)
    for num in l:
        sum += num
    average = sum / length
    return average 

def method_average(l):
    return sum(l)/len(l)

l = [1, 2, 3, 4, 5, 6, 7]

print('Average of list using simple method:', simple_average(l))
print('Average of list using library function method:', method_average(l))
