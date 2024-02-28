def search(nums, target):
    """
    Idea is - if we divide the nums array at any point in two parts one of the parts will be always sorted. 
    We will find if the element exist in the sorted part. 
    If it exists - 
        apply binary search to find the position of that element
    If it doesn't exist - 
        repeat the process of dividing array and selecting sorted part and search in that again
    If we are unable to find the element then returns -1
    """

    # initialization 
    start, end = 0, len(nums) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(target == nums[mid]):
            return mid

        # checking if left part is sorted:
        if(nums[start] <= nums[mid]):
            # checking if target lies in left part:
            if(target <= nums[mid] and nums[start] <= target):
                end = mid - 1
            # eliminate left part of array from consideration
            else:
                start = mid + 1
        # otherwise the right part is sorted since one of parts must be always sorted 
        else:
            # checking if target lies in this right part:
            if(target >= nums[mid] and target <= nums[end]):
                start = mid + 1
            # eliminate right part
            else:
                end = mid - 1 
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))
