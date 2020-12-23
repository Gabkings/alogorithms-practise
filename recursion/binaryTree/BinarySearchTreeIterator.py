'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BinarySearchTreeTreeIterator:
    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # stack to append tree nodes 
        self.stack = []
        # root node or the tree
        current = root
        while current is not None:
            # append the tree nodes into to the stack
            self.stack.append(current)
            current = current.left
        return
    
    def hasNext(self):
        return len(self.stack) != 0
    
    def next(self):
        next_node = self.stack.pop()
        current = next_node.right
        while current is not None:
            self.stack.append(current)
            current = current.left 
        return next_node
