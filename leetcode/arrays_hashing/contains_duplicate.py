def contains_duplicate_first(nums):
    """
    This is the linear search (naive) way to get
    to the solution. In this solution, two nested
    for loops are used to iterate over list. The
    outer loop keeps track of element that is being
    compared with the rest of elements by the 
    second loop which iterates through whole list.
    
    Time Complexity - O(n^2)
    Space Complexity - O(1)
    """
    if(len(nums) == 1 or len(nums) == 0):
        return False
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if(nums[i] == nums[j]):
                return True
    return False
        
def contains_duplicate_second(nums):
    """
    Using this approach, the list is first sorted. 
    Then, the two index variables which iterate
    over the list to find if they are duplicate.

    Time Complexity - O(nlogn)
    Space Complexity - O(1)
    """
    if(len(nums) == 1 or len(nums) == 0):
        return False
    nums.sort()
    i, j = 0, 1
    for i in range(len(nums)-1):
        if(nums[i] == nums[j]):
            return True
        j += 1
    return False

def contains_duplicate_third(nums):
    """
    In this approach, the list is first sorted,
    then using set function, which stores all unique
    values, the length of the set is compared with 
    length of list. This works since the set only 
    stores the unique elements.

    Time Complexity - O(nlogn)
    Space Complexity - O(1)
    """
    if(len(nums) == 1 or len(nums) == 0):
        return False
    nums.sort()
    if(len(set(nums)) != len(nums)):
        return True
    else:
        return False

def contains_duplicate_fourth(nums):
    """
    In this approach, a set is defined and
    the elements are being added from the given 
    list to the set. Since, set only adds unique
    elements, it will inform if element being
    added is already present in set
    
    Time Complexity - O(n)
    Space Complexity - O(n)
    """
    hashset = set()
    for num in nums: 
        if num in hashset: 
            return True
        hashset.add(num)
    return False

# True Case: 
nums = [1,1,1,3,3,4,3,2,4,2]
# False Case: 
#nums = [1,2,3,4]

print(contains_duplicate_first(nums))
print(contains_duplicate_second(nums))
print(contains_duplicate_third(nums))
print(contains_duplicate_fourth(nums))
