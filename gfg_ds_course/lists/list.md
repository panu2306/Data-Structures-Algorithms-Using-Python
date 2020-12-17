### Following are different list methods and their usage are provided with examples:
1. Index Method: 
    The index() method returns the index of the specified element in the list.
    - Usage: 
        list.index(element, start, end)
    - The list index() method can take a maximum of three arguments:
        :- element - the element to be searched
        :- start (optional) - start searching from this index
        :- end (optional) - search the element up to this index

2. Append Method: 
    The append() method adds an item to the end of the list.
    - Usage: 
        list.append(item)
    - The method takes a single argument
        :- item - an item to be added at the end of the list

3. Extend Method: 
    The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
    - Usage:
        list1.extend(iterable) #Here, all the elements of iterable are added to the end of list1.

4. Insert Method:
    The list insert() method inserts an element to the list at the specified index.
    - Usage:
        list.insert(i, elem)

5. Remove Method:
    The remove() method removes the first matching element (which is passed as an argument) from the list.
    - Usage: 
        list.remove(element)
    - remove() Parameters:
       :-  The remove() method takes a single element as an argument and removes it from the list.
       :-  If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.
6. Count Method: 
    The count() method returns the number of times the specified element appears in the list.
    - Usage: 
        list.count(element)
    - The count() method takes a single argument: 
        :- element - the element to be counted

7. Pop Method: 
    The pop() method removes the item at the given index from the list and returns the removed item.
    - Usage: 
        list.pop(index)
    - pop() parameters:
        :- The pop() method takes a single argument (index).
        :- The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
        :- If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.

8. Reverse Method:
    The reverse() method reverses the elements of the list.
    - Usage: 
        list.reverse()
    - The reverse() method doesn't take any arguments.

9. Sort Method:
    The sort() method sorts the elements of a given list in a specific ascending or descending order.
    - Usage: 
        list.sort(key=..., reverse=...)
    - By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
        :- reverse - If True, the sorted list is reversed (or sorted in Descending order)
        :- key - function that serves as a key for the sort comparison

10. Copy Method: 
    The copy() method returns a shallow copy of the list.

11. Clear Method: 
    The clear() method removes all items from the list.
    - Usage: 
        list.clear()

### Example illustrating all above mentioned methods: 
```
    def index_implementation(arr):
        print(arr.index('p'))
        print(arr.index('q', 3, len(arr)))  # this will search for element 'q' from 3rd position to the end of list

    def append_implementation(arr):
        element = 100
        arr.append(element)
        print('List after appending: ', arr)
        small_list = [1,2,3]
        arr.append(small_list)
        print('List after appending another list: ', arr)

    def extend_implementation(arr):
        temp_list = [1,2,3]
        arr.extend(temp_list)
        print('List after extending operation: ', arr)

    def insert_implementation(arr):
        element = 200
        arr.insert(0, 200)
        print('List after insertion of element: ', arr)

    def remove_implementation(arr):
        element = 100
        arr.remove(element)
        print('List after removal of element: ', arr)

    def count_implementation(arr):
        element = 100
        print('Count of element 100: ', arr.count(element))

    def pop_implementation(arr):
        arr.pop() #removes last indexed element
        arr.pop(3) #removes elements at index 3
        print('List after pop of element: ', arr)

    def reverse_implementation(arr):
        arr.reverse()
        print('List after reversal of elements: ', arr)

    def sort_implementation(arr):
        arr.sort()
        print('List after sort of elements: ', arr)

    def copy_implementation(arr):
        new_arr = arr.copy() #shallow-copy
        print('new list after copying from list1: ', new_arr))

    def clear_implementation(arr):
        arr.clear()
        print('List after insertion of element: ', arr)


    if(__name__== '__main__'):
        arr = ['a', 'i', 'o', 'p', 'q']
        
        index_implementation(arr)
        append_implementation(arr)
        extend_implementation(arr)
        insert_implementation(arr)
        remove_implementation(arr)
        count_implementation(arr)
        pop_implementation(arr)
        reverse_implementation(arr)
        #sort_implementation(arr)
        copy_implementation(arr)
        clear_implementation(arr)
```
