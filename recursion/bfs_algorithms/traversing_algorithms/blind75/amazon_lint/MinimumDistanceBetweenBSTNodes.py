

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


''' 
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
'''

class Solution:

    def min_diff_in_bst(self, root: TreeNode):
        self.ans = float('inf')
        self.pre = -1 
        self.dfs(root)

        return self.ans

    def dfs(self, root):
        if not root:
            return None 
        self.dfs(root.left)
        if self.pre == -1:
            self.pre = root.val 

        else:
            self.ans = min(self.ans, root.val - self.pre)
            self.pre = root.val 
        self.dfs(root.right)

    def inorderTraversal(self, root: TreeNode):
            
        values = []
        
        stack = [root]
        
        while stack:
            
            top = stack[-1]
            stack.pop()
            
            if type(top) == int:
                values.append(top)
            elif top is not None: # top is a TreeNode obj
                stack.append(top.right)
                stack.append(top.val)
                stack.append(top.left)
            
        return values


root = {4,2,6,1,3}

sln = Solution()

print(sln.min_diff_in_bst(root))