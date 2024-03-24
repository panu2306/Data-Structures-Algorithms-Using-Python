"""
Approach - 1 : Sliding Window and Hashmap (Counter class)
    Time Complexity: O(26 * n)
    Space Complexity: O(n)
"""
def characterReplacement_1(s, k):
    count = {}
    max_substr_len = 0
    l = r = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while((r-l+1) - max(count.values()) > k):
            count[s[l]] -= 1
            l += 1
        max_substr_len = max(max_substr_len, r-l+1)
    return max_substr_len

"""
Approach - 2 : Sliding Window and Hashmap (Counter class) with optimization using max_frequency 
    Time Complexity: O(n)
    Space Complexity: O(n)
"""
def characterReplacement_2(s, k):
    count = {}
    max_substr_len = 0
    l = r = 0
    max_frequency = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_frequency = max(max_frequency, count[s[r]])
        while((r-l+1) - max_frequency > k):
            count[s[l]] -= 1
            l += 1
        max_substr_len = max(max_substr_len, r-l+1)
    return max_substr_len


s = "AABABBA"
k = 1
print("Using sliding window: ", characterReplacement_1(s, k))
print("Using slinding window and optimization: ", characterReplacement_2(s, k))
