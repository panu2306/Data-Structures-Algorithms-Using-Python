"""
Approach - 1 (using built-in method - reversed)
Time Complexity: O(n)
Space Complexity: O(n)
"""
def isPalindrome_1(s):
    filtered_string = filter(lambda c: c.isalnum(), s)
    lowercased_string = map(lambda c: c.lower(), filtered_string)
    filtered_chars_list = list(lowercased_string)
    reversed_chars_list = list(reversed(filtered_chars_list))
    return filtered_chars_list == reversed_chars_list

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def isPalindrome_2(s):
    left, right = 0, len(s)-1
    while(left < right):
        while(left < right and not s[left].isalnum()):
            left += 1
        while(left < right and not s[right].isalnum()):
            right -= 1

        if(s[left].lower() != s[right].lower()):
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"
print("Is valid palindrome? ", isPalindrome_1(s))
print("Is valid palindrome? ", isPalindrome_2(s))
