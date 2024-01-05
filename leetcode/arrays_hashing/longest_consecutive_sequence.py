"""
Using brute-force: 
    Time Complexity: O(n^3)
    Space Complexity: O(1)
"""
def longestConsecutive_0(nums):
    longest = 0
    for num in nums:
        current_longest = 1
        current_num = num

        while(current_num+1 in nums):
            current_longest += 1
            current_num += 1

        longest = max(longest, current_longest)
    return longest


"""
Using sort method:
    Time-Complexity: O(nlogn)
    Space-Complexity: O(1)
"""
def longestConsecutive_1(nums):
    if(not nums):
        return 0
    nums.sort()
    longest = 1
    current_longest = 1
    for i in range(1, len(nums)):
        if(nums[i] != nums[i-1]):
            if(nums[i-1]+1 == nums[i]):
                current_longest += 1
                longest = max(longest, current_longest)
            else:
                current_longest = 1
    return max(longest, current_longest)



"""
"""
def longestConsecutive_2(nums):
    nums_set = set(nums)
    longest_streak = 0
    for num in nums:
        if(num-1 not in nums_set):
            current_streak = 1
            current_num = num

            while((current_num+1) in nums_set):
                current_streak += 1
                current_num += 1

            longest_streak = max(current_streak, longest_streak)
    return longest_streak
    

nums = [0,3,7,2,5,8,4,6,0,1, 16, 15]
print("************* Longest Consecutive Sequence **********************")
print("Using Brute-Force: ", longestConsecutive_0(nums))
print("Using Sort: ", longestConsecutive_1(nums))
print("Using Hashmap: ", longestConsecutive_2(nums))

