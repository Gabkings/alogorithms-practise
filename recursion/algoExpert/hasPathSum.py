# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: 
        sums = []
        
        calculateSums(root, 0, sums)
        print(calculateSums(root,0,sums))
        
        for i in range(len(sums)):
            if sums[i] == targetSum:
                return True
        return False
    
def calculateSums(root, runningSum, sums):
    
    if root is None:
        return sums

    newRunningSum = runningSum + root.val
    
    if root.left is None and root.right is None:
        sums.append(newRunningSum)
        return
    calculateSums(root.left, newRunningSum, sums )
    calculateSums(root.right, newRunningSum, sums )
    
    return sums
    
    
 