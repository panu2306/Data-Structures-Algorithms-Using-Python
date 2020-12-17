def largest(l):
    maximum = l[0]
    if not l:
        return None
    else:
        for num in l: 
            if(num>maximum):
                maximum = num
        return maximum


l = [2, 4, 3, 9, 6, 5, 8]

print('Largest number in list:', largest(l))