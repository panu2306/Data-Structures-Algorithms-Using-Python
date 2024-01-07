"""
Approach 1: Slinding Window and Counter:
    Time-Complexity: O(n)
    Space-Complexity: O(n)
"""
from collections import Counter

def lengthOfLongestSubstring_1(s):
    chars = Counter()
    left = right = 0
    res = 0
    while(right < len(s)):
        r = s[right]
        chars[r] += 1
        while(chars[r] > 1):
            l = s[left]
            chars[l] -= 1
            left += 1
        res = max(res, right-left+1)
        right += 1
    return res

"""
Approach 2: Sliding Window and Set:
    Time-Complexity: O(n)
    Space-Complexity: O(n)
"""
def lengthOfLongestSubstring_2(s):
    subset = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while(s[r] in subset):
            subset.remove(s[l])
            l += 1
        subset.add(s[r])
        res = max(res, r-l+1)
    return res

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
print("Length of longest substring: ", lengthOfLongestSubstring_1(s))
print("Length of longest substring: ", lengthOfLongestSubstring_2(s))
