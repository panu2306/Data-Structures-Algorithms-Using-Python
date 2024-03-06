def searchRange(nums, target):
    start = binary_search(nums, target, True)
    end = binary_search(nums, target, False)
    return [start, end]

def binary_search(nums, target, leftBias):
    left, right = 0, len(nums)-1
    while(left <= right):
        mid = (left + right) // 2
        if(nums[mid] == target):
            if(leftBias):
                if(left == mid or nums[mid-1] < target):
                    return mid 
                right = mid - 1
            else:
                if(mid == right or nums[mid+1] > target):
                    return mid
                left = mid + 1
        elif(nums[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [5,7,7,8,8,10]
target = 10

print(searchRange(nums, target))
