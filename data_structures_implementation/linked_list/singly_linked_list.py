class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # append node : 
    def append(self, data):
        new_node = Node(data)
        self.size += 1
        # head is none:
        if(self.head is None):
            self.head = new_node
            self.head.next = None
        else:
            curr = self.head
            while(curr.next is not None):
                curr = curr.next
            curr.next = new_node
        

    # search node with given value : 
    def search(self, value):
        curr = self.head
        while(curr.next is not None and curr.data != value):
            curr = curr.next
        if(curr.data == value):
            return True
        else:
            return False

    # delete a node with given value : 
    def delete(self, value):
        curr = self.head
        prev = None
        if(curr.data == value):
            prev = curr
            self.head = curr.next
            prev.next = None
            self.size -= 1
        else:
            while(curr.next is not None and curr.data != value):
                prev = curr
                curr = curr.next
            # value is found
            if(curr.data == value):
                prev.next = curr.next
                curr.next = None
                self.size -= 1
            else:
                curr.data = None
                curr.next = None


    # traverse through all the nodes : 
    def traverse(self):
        curr = self.head
        while(curr.next):
            print(curr.data, end="  ")
            curr = curr .next
        print(curr.data)

    # return the current size of linked list : 
    def size(self):
        return self.size


sll = SinglyLinkedList()
sll.append(11)
sll.append(12)
sll.append(13)
sll.append(14)
sll.append(15)
print("Singly linked list: ")
sll.traverse()
print("current size of singly linked list: ", sll.size)
print("Is element present? ", sll.search(1))
print("deleting an element from the linked list....")
sll.delete(11)
print("Singly linked list after deletion: ")
sll.traverse()
print("current size of singly linked list: ", sll.size)
