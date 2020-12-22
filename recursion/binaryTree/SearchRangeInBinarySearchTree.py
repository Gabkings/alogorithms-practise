'''
Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

Example
Example 1:

Input：{5},6,10
Output：[]
        5
it will be serialized {5}
No number between 6 and 10
Example 2:

Input：{20,8,22,4,12},10,22
Output：[12,20,22]
Explanation：
        20
       /  \
      8   22
     / \
    4   12
it will be serialized {20,8,22,4,12}
[12,20,22] between 10 and 22
'''

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        
        self.helper(root, k1, k2, result)

        return result 
        
    def helper(self, root, k1, k2, result):
        # write your code here
        if not root:
            return None 
            
        if root.val > k1:
            self.helper(root.left, k1, k2, result)
            
        if k1 <= root.val <= k2:
            result.append(root.val)
            
        if root.val < k2:
             self.helper(root.right, k1, k2, result)