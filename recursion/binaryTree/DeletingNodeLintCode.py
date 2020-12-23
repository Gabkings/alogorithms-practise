"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    
    # get the minmum node value
    def minmunValue(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
        
    # case 1: the node to be deleted is a leaf node
    # we just delete the node straight away
    # case 2: the node to be deleted has child
    # we delete the node and replace the parent with child node 
    # case 3: The node to be deleted has two children
    #  Find the successor of the node on the right tree,
    #  Replace the value of node to delete with successor value
    # minmunValue(root) returns the successor node value 
    def removeNode(self, root, value):
        # write your code here
        current = root
        value = value
        
        if current is None:
            return
        
        if value < current.val:
            current.left = self.removeNode(current.left, value)
        elif value > current.val:
            current.right = self.removeNode(current.right, value)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            
            if current.right is None:
                temp = current.left
                self.current = None
                return temp
            temp = self.minmunValue(current.right)
            current.val = temp.val
            current.right = self.removeNode(current.right, temp.val)
        return current
        
        
