"""
    # Mathod 1 : 
    # Uses first range of row elements to choose row in which element lies and then applies binary
    # search on that row.
    # Time Complexity = O(m*logn)
    # Space Complexity = O(1)

def binary_search(row, target):
    left, right = 0, len(row) - 1
    while(left <= right):
        mid = (left + right) // 2
        if(row[mid] == target):
            return True
        elif(row[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return False

def searchMatrix(matrix, target):
    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if(matrix[i][0] <= target <= matrix[i][row_len-1]):
            return binary_search(matrix[i], target)
"""

"""
Method 2 : 
    Considers whole matrix as a 1-D array and then applies a binary search
    Crux of Solution - Find the element in 2D array using index of considered 1D array
                     - To find use the formula to calculate the row_id and col_id: 
                            row_id = index // n 
                            col_id = index % n  => since column numbers will range from 0 to n-1
"""

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n - 1
    
    while(left <= right):
        index = (left + right) // 2
        index_ele = matrix[index // n][index % n]
        if(index_ele == target):
            return True
        elif(index_ele < target):
            left = index + 1
        else:
            right = index - 1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

print(searchMatrix(matrix, target))
