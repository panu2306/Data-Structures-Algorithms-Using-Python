def linear_search(array, element):
	for i in range(len(array)):
		if(array[i] == element):
			return 1
	

array = [1, 3, 4, 2, 6, 5]
element = 6

result = linear_search(array, element)

if(result==1):
	print("Element is Present") 
else:
	print("Element is Absent")
	
