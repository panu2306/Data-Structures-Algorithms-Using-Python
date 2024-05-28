class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # to check if stack is empty
    def is_empty(self):
        return self.size == 0

    # push to stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return "Pushed"

    # pop from the stack
    def pop(self):
        if(self.size == 0):
            return "Stack is empty, can't perform pop operation"
        curr_node = self.head
        self.head = self.head.next
        curr_node.next = None
        self.size -= 1
        return "Popped"


    # get the top of stack 
    def peek(self):
        return self.head.data

    # list stack values
    def display(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.data, end="  ")
            curr_node = curr_node.next
        return 

stack = Stack()
print(stack.push(10))
print(stack.push(20))
print(stack.push(30))
print(stack.display())  # Stack: [30, 20, 10]

print("Top element is", stack.peek())  # Top element is 30

print(stack.pop())
print(stack.display())  # Stack: [20, 10]
