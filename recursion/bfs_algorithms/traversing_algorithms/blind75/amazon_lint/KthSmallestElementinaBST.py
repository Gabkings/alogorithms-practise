
import collections
class Solution:

    '''
    Given the root of a binary search tree, and an integer k,
    return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
    '''

    def kthSmallest(self, root, k):
        return self.dfs(root)[k-1]

    def dfs(self, root):
        return self.dfs(root.left) + [root.val] + self.dfs(root.right) if root else []



    def inorderSuccessor(self, root, p):
        '''
        Given a binary search tree (See Definition) and a node in it, 
        find the in-order successor of that node in the BST.

        If the given node has no in-order successor in the tree, return null.
        '''

        stack = []

        lastnode = None
        n, res = root, None 

        while n is not None:
            stack.append(n)
            n = n.left 

        while stack:
            node = stack[-1]
            if lastnode and lastnode == p:
                res = node 
            lastnode = node
            if node.right is not None:
                node = node.right 
                while node is not None:
                    stack.append(node)
                    nod = node.left 
            else:
                n = stack.pop()
                while stack and stack[-1].right == n:
                    n = stack.pop() 
        return res 

    
    def rangeSumBST(self, root, low, high):
        total = 0
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            if node.val > high:
                q.append(node.left)
            elif node.val < low:
                q.append(node.right)
            else:
                total += node.val
                q.append(node.left)
                q.append(node.right)

        return total