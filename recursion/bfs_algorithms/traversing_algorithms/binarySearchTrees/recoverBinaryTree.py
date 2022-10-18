
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

class Solution:
    def recoverTree(self, root):
        self.first, self.second, self.prev = None, None, TreeNode(float('-inf')) 
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev.val >= node.val: 
                    self.first = self.first or self.prev
                    self.second = node
                self.prev = node
                inorder(node.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val