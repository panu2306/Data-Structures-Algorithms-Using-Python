def two_sums_first(nums, target):
    """
    In this approach, the brute force is used. 
    Here, two nested for loops are used. One for 
    loop keeps track of first element and second for
    loop to find another element whose sum with first 
    element, if came equal to the target, then the indexes
    of both elements are returned. 

    Time Complexity: O(n^2)
    """
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if(nums[j] > target):
                continue
            if(nums[i] + nums[j] == target):
                return [i, j]

def two_sums_second(nums, target):
    """
    In this approach, a hashmap can be used to store the 
    visited number and its index. Firstly, through a for loop, 
    each number is visited and subtracted from target and the result 
    of subtraction is then looked into the hashmap if it is present.
    If the result is present that means the two numbers can be added to
    get the target. If the result is not in hashmap already then the corresponding
    number is added to the hashmap and loop continues till the result is found in 
    hashmap.
    """
    hashmap = {}
    for i, num in enumerate(nums):
        remainder = target - num
        if(remainder not in hashmap):
            hashmap[num] = i 
        else:
            return [i, hashmap[remainder]]

            


nums = [2, 3, 5, 12, 6, 3]
target = 6
print(two_sums_first(nums, target))
print(two_sums_second(nums, target))
