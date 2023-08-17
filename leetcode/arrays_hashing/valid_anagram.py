def isAnagram_first(s, t):
    """
    In this approach, sorted() function is 
    used which basically sorts the string based
    on each character's ascii values. Therefore, 
    two returned lists of characters of strings 
    are compared. It returns true if they are equal. 

    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    return sorted(s) == sorted(t)

def isAnagram_second(s, t):
    """
    In this approach, hashmap is used to store
    the occurance of each character in both string. 
    Two hashmaps are used one for each string. 
    After storing occurances, using for loop the occurance
    of each character of first string is compared with 
    the occurance of that character in the second string. 
    If there's no match of count of occurance or even the
    character of first string doesn't exist in another, False
    value is returned. 

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if(len(s) != len(t)):
        return False

    s_map, t_map = {}, {}
    for i in range(len(s)):
        s_map[s[i]] = 1 + s_map.get(s[i], 0)
        t_map[t[i]] = 1 + t_map.get(t[i], 0)
    for key in s_map:
        if(s_map[key] != t_map.get(key, 0)):
                return False
    return True
    
s = "anagram"
t = "nagaram"
print(isAnagram_first(s, t))
print(isAnagram_second(s, t))
