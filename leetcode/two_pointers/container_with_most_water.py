"""
Approach - 1 (Brute-Force):
    Time-Complexity: O(n^2)
    Space-Complexity: O(1)
"""
def maxArea_1(heights):
    max_area = 1
    length = len(heights)
    for i in range(0, length):
        for j in range(1, length):
            current_area = (j-i) * min(heights[i], heights[j])
            max_area = max(max_area, current_area)
    return max_area 


"""
Approach - 2 (Two-Pointer Approach)
"""
def maxArea_2(heights):
    start, end = 0, len(heights) - 1
    max_area = 1
    while(start < end):
        current_area = (end - start) * min(heights[start], heights[end])  # width * height
        max_area = max(max_area, current_area)
        if(heights[start] <= heights[end]):
            start += 1
        else:
            end -= 1
    return max_area

heights = [1,8,6,2,5,4,8,3,7]
#heights = [1,1]
print("Container with Maximum Area: ", maxArea_1(heights))
print("Container with Maximum Area: ", maxArea_2(heights))
