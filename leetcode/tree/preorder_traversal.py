"""
Program solution for PreOrder Tree Traversal - Iterative
Note: Solution can be only run in leetcode.
"""

class Solution:
    def preorder_traversal(self, root):
        # Root -> Left -> Right
        result = []
        stack = []
        if(root is None):
            return result
        stack.append(root)
        
        while(stack):
            root = stack[-1]
            stack.pop()
            result.append(root.val)
            if(root.right):
                stack.append(root.right)
            if(root.left):
                stack.append(root.left)
        return result

# root = [1, null, 2, 3]

