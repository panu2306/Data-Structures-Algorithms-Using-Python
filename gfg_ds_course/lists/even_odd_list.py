def using_simple_method(l):
    l1 = []
    l2 = []
    for num in l:
        if(num%2 == 0):
            l1.append(num)
        else:
            l2.append(num)
    return l1, l2 

def using_list_comprehension(l):
    return  [num for num in l if(num%2 == 0)], [num for num in l if(num%2 != 0)]

l = [1, 2, 3, 4, 5, 6, 7, 8]

print('Using `LIST-COMPREHENSION`: Even list from main list: {} and odd list from main list: {}'.format(using_list_comprehension(l)[0],using_list_comprehension(l)[1]))
print('Using `SIMPLE METHOD`: Even list from main list: {} and odd list from main list: {}'.format(using_simple_method(l)[0], using_simple_method(l)[0]))