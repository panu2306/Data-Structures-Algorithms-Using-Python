def twoSum(nums, target):
    left, right = 0, len(nums)-1
    while(left <= right):
        addition = nums[left] + nums[right]
        if(addition == target):
            return [left+1, right+1]
        elif(addition < target):
            left += 1
        else:
            right -= 1
            
numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))

