def using_list_comprehension(l, key):
    return [num for num in l if(num<key)]

def using_simple_method(l, key):
    small_numbered_list = []
    for num in l:
        if(num<key):
            small_numbered_list.append(num)
    return small_numbered_list

l = [5, 10, 15, 20, 1, 5, 30]
key = 10

print('List of elements smaller than given key number using list-comprehension method:', using_list_comprehension(l, key))
print('List of elements smaller than given key number using simple method:', using_simple_method(l, key))
