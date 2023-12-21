"""
# brute-force aproach:
Space Complexity = O(1)
Time Complexity = O(n^2)
"""
def product_array(nums):
    length = len(nums)
    result_array = []
    for i in range(length):
        product = 1
        for j in range(i+1, length):
            product = product * nums[j]
        for j in range(0, i):
            product = product * nums[j]
        result_array.append(product)
    return result_array

"""
# Prefix and suffix product with an extra array approach:
Space Complexity = O(n)
Time Complexity = O(n)
"""
def product_array_1(nums):
    left_product = []
    right_product = []
    length = len(nums)
    
    prefix_product = 1
    left_product.append(prefix_product)
    for i in range(1, length):
        prefix_product = prefix_product * nums[i-1]
        left_product.append(prefix_product)
    
    suffix_product = 1
    right_product.append(suffix_product)
    for i in range(length-2, -1, -1):
        suffix_product = suffix_product * nums[i+1]
        right_product.append(suffix_product)

    answer = []
    for i in range(length):
        answer.append(left_product[i] * right_product[length-1-i])
    return answer

"""
# Prefix and suffix product without and extra array approach:
Space Complexity = O(1)
Time Complexity = O(n)
"""
def product_array_2(nums):
    answer = []
    length = len(nums)
    prefix_product = 1
    answer.append(prefix_product)
    for i in range(1, length):
        prefix_product = prefix_product * nums[i-1]
        answer.append(prefix_product)
    
    suffix_product = 1 
    answer[length-1] = suffix_product * answer[length-1]
    for i in range(length-2, -1, -1):
        suffix_product = suffix_product * nums[i+1]
        answer[i] = suffix_product * answer[i]
    return answer

nums = [1,2,3,4]
print("************ Product of Array Without Self *********")
print("Using brute-force approach: ", product_array(nums))
print("Using prefix and suffix with extra array approach: ", product_array_1(nums))
print("Using prefix and suffix product approach: ", product_array_2(nums))

