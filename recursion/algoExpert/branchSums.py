class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def branchSums(root):
    # initial sum list 
    sums = []
    
    calculateBranchSums(root, 0, sums)
    
    return sums

def calculateBranchSums(root, runningSum, sums):
    # Edge case for node with no children
    if root is None:
        return 
    
    newRunningSum = runningSum + root.value
    if root.left is None and root.right is None:
        sums.append(newRunningSum)
        return
    calculateBranchSums(root.left, newRunningSum, sums)
    
    calculateBranchSums(root.right, newRunningSum, sums)
    