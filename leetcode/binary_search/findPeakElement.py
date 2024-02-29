def findPeakElement(nums):
    # nums has only one element
    if(len(nums) == 1):
        return 0
    # first element is peak element
    if(nums[0] > nums[1]):
        return 0
    # last element is peak element
    if(nums[-1] > nums[-2]):
        return len(nums)-1

    left, right = 0, len(nums)-1
    while(left <= right):
        mid = (left + right) // 2
        if(nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]):
            return mid
        elif(nums[mid] < nums[mid+1]):
            left = mid + 1
        else:
            right = mid - 1


nums = [1, 2, 1, 3, 5, 6, 4]
print("Index of the peak element in the given list: ", findPeakElement(nums))
