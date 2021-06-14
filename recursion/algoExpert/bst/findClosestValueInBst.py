
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelperV2(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest
    
def findClosestValueInBstHelperV2(tree, target, closest):
    currentNode = tree
    
    while currentNode is not None:
        
    
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > tree.value:
            currentNode = currentNode.right
        else:
            break
    return closest

tree = BST(12)

print(findClosestValueInBst(tree, 12))
    


