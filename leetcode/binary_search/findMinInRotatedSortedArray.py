def findMin(nums):
    minimum = nums[0]
    left, right = 0, len(nums)-1
    while(left <= right):
        mid = (left + right) // 2
        if(nums[left] <= nums[right]):
            minimum = min(minimum, nums[left])
            break
        if(nums[left] <= nums[mid]):
            minimum = min(minimum, nums[left])
            left = mid + 1
        else:
            minimum = min(minimum, nums[mid])
            right = mid - 1 
    return minimum

nums = [5,6,7,0,1,2,3,4]
print(findMin(nums))
