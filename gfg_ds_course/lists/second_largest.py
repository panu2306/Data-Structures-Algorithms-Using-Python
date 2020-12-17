def second_largest(l):
    largest = max(l)
    second_largest = None
    if(len(l)<=1):
        return None
    else:
        for num in l:
            if(num != largest):
                if(second_largest == None):
                    second_largest = num
                else:
                    second_largest = max(second_largest, num)
    return second_largest

def efficient_second_largest(l):
    largest = l[0]
    second_largest = l[0]
    if(len(l)<=1):
        return None
    else:
        for num in l:
            if(num>largest):
                second_largest = largest
                largest = num
            elif(num!=largest):
                if(num>second_largest):
                    second_largest = num
    return second_largest

l = [5, 20, 12, 10, 20, 10, 12]
print('Second largest using simple method:', second_largest(l))
print('Second largest using efficient method:', efficient_second_largest(l))
