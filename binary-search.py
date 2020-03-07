# Binary Search Algorithm Implementation Using Python
def binary_search(start, end, sorted_list, ele):
	if(end >= start):
		mid = (start + end) // 2
		if(ele == sorted_list[mid]):
			return ele

		elif(ele > sorted_list[mid]):
			start = mid + 1
			return binary_search(start, end, sorted_list, ele)
	
		else: 
			end = mid - 1 
			return binary_search(start, end, sorted_list, ele)
	return -1

ele = int(input("Enter element to search:"))
list1 = [6, 3, 7, 1, 2, 5, 4]
sorted_list = sorted(list1)
start = 0
end = len(sorted_list) - 1
result = binary_search(start, end, sorted_list, ele)
print("Element is present") if result == ele else print("Element is not present")



