class ArrayBinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size
    
    def root(self, value):
        if(self.tree[0] == None):
            self.tree[0] = value
        else:
            print("Tree already has a root")

    def set_left(self, val, parent):
        if(self.tree[parent] == None):
            print("No parent is present")
        else:
            self.tree[ (2 * parent) + 1] = val

    def set_right(self, val, parent):
        if(self.tree[parent] == None):
            print("No parent is present")
        else:
            self.tree[ (2 * parent) + 2] = val

    def print_tree(self):
        for i in range(self.size):
            if(self.tree[i] != None):
                print(self.tree[i], end=" ")
            else:
                print("_", end=" ")
        print()

abt = ArrayBinaryTree(10)
abt.root('A')
abt.set_left('B', 0)
abt.set_right('C', 0)
abt.set_left('D', 1)
abt.set_right('E', 1)
abt.set_right('F', 2)
abt.print_tree()
