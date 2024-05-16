from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class LinkedBinaryTree:
    def __init__(self):
        self.root = None

    # Insert node into binary tree: queue is used to keep track of elements
    def insert_node(self, data):
        new_node = Node(data)
        if(self.root == None):
            # create a root node
            self.root = new_node
            return self.root
        q = deque()
        q.append(self.root)
        while(q):
            temp = q.popleft()
            if(temp.left != None and temp.right != None):
                q.append(temp.left)
                q.append(temp.right)
            else:
                if(temp.left == None):
                    temp.left = new_node
                    q.append(temp.left)
                else:
                    temp.right = new_node
                    q.append(temp.right)
                break
    
    # Inorder Traversal : Left -> Root -> Right
    def inorder_traversal(self, node): 
        if(self.root == None):
            print("Tree is empty!")
            return 
        else:
            if(node.left is not None): 
                self.inorder_traversal(node.left)
            print(node.data, end="  ")
            if(node.right is not None):
                self.inorder_traversal(node.right)

    # Preorder Traversal : Root -> Left -> Right
    def preorder_traversal(self, node):
        if(self.root == None):
            print("Tree is empty!")
        else:
            print(node.data, end="  ")
            if(node.left is not None):
                self.preorder_traversal(node.left) 
            if(node.right is not None):
                self.preorder_traversal(node.right)
    
    # Postorder Traversal : Left -> Right -> Root
    def postorder_traversal(self, node):
        if(self.root == None):
            print("Tree is empty!")
            return
        else:
            if(node.left is not None):
                self.postorder_traversal(node.left)
            if(node.right is not None):
                self.postorder_traversal(node.right)
            print(node.data, end="  ")

    # Level Order Traversal : 
    def levelorder_traversal(self, node):
        if(self.root is None):
            print("Tree is empty!")
        else:
            q = deque()
            q.append(node)
            while(q):
                temp = q.popleft()
                print(temp.data, end="  ")
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)

    
lbt = LinkedBinaryTree()
lbt.insert_node(1)
lbt.insert_node(2)
lbt.insert_node(3)
lbt.insert_node(4)
lbt.insert_node(5)
lbt.insert_node(6)
lbt.insert_node(7)
print("Inorder Tree Traversal: ")
lbt.inorder_traversal(lbt.root)
print()
print("Preorder Tree Traversal: ")
lbt.preorder_traversal(lbt.root)
print()
print("Postorder Tree Traversal: ")
lbt.postorder_traversal(lbt.root)
print()
print("Levelorder Tree Traversal: ")
lbt.levelorder_traversal(lbt.root)
print()
