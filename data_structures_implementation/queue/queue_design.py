# Queue Implementation: 
class Queue: 
    def __init__(self):
        self.queue = []
        self.front = 0

    # enqueue: insert element into queue
    def enqueue(self, item):
        self.queue.append(item)
        return True

    # dequeue: delete front from queue
    def dequeue(self):
        if(self.is_empty()):
            return False
        self.front += 1
        return True

    # get front of the queue
    def front(self):
        return self.queue(self.front)

    # checking if queue is empty or not
    def is_empty(self):
        return self.front >= len(self.queue)
"""
# Limita0tion of above implementation of queue: 
We cannot insert new element in the queue when queue is full and we have also dequeued the element to get new element because we can't use the dequeued element's place to allocate to new element since dequeue happens on first element of the queue and enqueue happens at last position. 

Solution ?? 

- Use of Circular Queue
    - Using array
    - Using Linked Linked List

"""

# Circular Queue Implementation Using Array: 
class CircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.front = 0
        self.count = 0 
        self.capacity = k

    def enqueue(self, item):
        if(self.is_full()):
            return -1
        self.queue[(self.front + self.count) % self.capacity] = item
        self.count += 1 
        return True
        
    
    def dequeue(self):
        if(self.is_empty()):
            return -1
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def get_front(self):
        if(self.is_empty()):
            return -1
        return self.queue[self.front]

    def get_back(self):
        if(self.is_empty()):
            return -1
        return self.queue[(self.front + self.count - 1) % self.capacity]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity


# Circular Queue Implementation Using Linked List:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedCircularQueue:
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.capacity = k
        self.count = 0

    def enqueue(self, item):
        if(self.is_full()):
            return False
        
        new_node = Node(item)
        
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.count += 1
        return True
            
    
    def dequeue(self):
        if(self.is_empty()):
            return False
        self.head = self.head.next
        self.count -= 1
        return True
    
    def get_front(self):
        if(self.is_empty()):
            return -1
        return self.head.value

    def get_back(self):
        if(self.is_empty()):
            return -1
        return self.tail.value

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.capacity == self.count

    def get_queue(self):
        curr = self.head
        while(curr):
            print(curr.value, "  ")
            curr = curr.next
        print("\n")
        return 


"""
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue.queue)
queue.dequeue()
print(queue.queue)
print(queue.front)
"""

choose = input("Which Implementation You want to perform - \n 1. Circular Queue Using Array \n 2. Circular Queue Using Linked List")
if(choose == "1"):
    circular_queue = CircularQueue(5)
    choice = -1
    while(choice != 0):
        choice = int(input("Select Option: 1. Enqueu 2. Dequeue 3. getFront 4. getBack 5. isEmpty 6. isFull 7. getQueue"))
        if(choice == 1):
            item = input("Enter Element: ")
            print(circular_queue.enqueue(item))
        elif(choice == 2):
            print(circular_queue.dequeue())
        elif(choice == 3):
            print(circular_queue.get_front())
        elif(choice == 4):
            print(circular_queue.get_back())
        elif(choice == 5):
            print(circular_queue.is_empty())
        elif(choice == 6):
            print(circular_queue.is_full())
        elif(choice == 7):
            print(circular_queue.get_queue())
        else:
            exit()
elif(choose == "2"):
    circular_queue = LinkedCircularQueue(5)
    choice = -1
    while(choice != 0):
        choice = int(input("Select Option: 1. Enqueu 2. Dequeue 3. getFront 4. getBack 5. isEmpty 6. isFull 7. getQueue"))
        if(choice == 1):
            item = input("Enter Element: ")
            print(circular_queue.enqueue(item))
        elif(choice == 2):
            print(circular_queue.dequeue())
        elif(choice == 3):
            print(circular_queue.get_front())
        elif(choice == 4):
            print(circular_queue.get_back())
        elif(choice == 5):
            print(circular_queue.is_empty())
        elif(choice == 6):
            print(circular_queue.is_full())
        elif(choice == 7):
            print(circular_queue.get_queue())
        else:
            exit()
else:
    print("invalid option")

