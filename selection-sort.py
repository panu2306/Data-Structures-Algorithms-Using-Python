def selection_sort(a):
	for i in range(len(a)):
		min_index = i
		for j in range(i+1, len(a)):
			if(a[min_index] > a[j]): 
				min_index = j

		a[i], a[min_index] = a[min_index], a[i]
	return a 

a = [64, 25, 10, 22, 11]
print(selection_sort(a))



	
