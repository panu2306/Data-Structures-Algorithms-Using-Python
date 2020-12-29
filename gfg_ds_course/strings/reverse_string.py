def reverse_using_for(s):
    s1 = ''
    for i in s:
        s1 = i + s1
    return s1

def reverse_using_recursion(s):
    if(len(s) == 0):
        return s
    else:
        return reverse_using_recursion(s[1:]) + s[0]

def reverse_using_built_in(s):
    return s[::-1]

s = input('Enter a string to reverse:')
print(reverse_using_for(s))
print(reverse_using_recursion(s))
print(reverse_using_built_in(s))
