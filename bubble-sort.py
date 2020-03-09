def bubble_sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]

array = [2, 4, 3, 1, 5]
bubble_sort(array)
print(array)