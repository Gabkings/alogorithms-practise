
from collections import deque
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ''' The same as above but converted to iterative solution using an explicit stack.
            The working and complexities should be about the same for both the solutions. 
            But, an interviewer may ocassionally ask to implement iterative version, so it's good to know this as well.
        '''
        s, tot_sum = deque([(root, 0)]), 0
        while(len(s)):
            root, cur = s.pop()
            cur = cur * 10 + root.val
            if not root.left and not root.right: 
                tot_sum += cur
            if root.right: 
                s.append((root.right, cur))
            if root.left: 
                s.append((root.left, cur))
        return tot_sum

    def sumNumbers(self, root):
        def dfs(root, cur):
            if not root: return 0
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                return cur
            return dfs(root.left, cur) + dfs(root.right, cur)
        return dfs(root, 0)