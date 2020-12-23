"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self,root, minValue, maxValue):
        root = root
        maxValue = maxValue
        minValue = minValue
        if root is None:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        validLeft = self.helper(root.left, minValue, root.val)
        validRight = self.helper(root.right, root.val, maxValue)
        return validRight and validLeft