class TreeNode:

    def __init__(self, val):
        self.val = val

        self.left, self.right = None, None 
from collections import deque
def tree_right_view(root):
    result = [] 
    if root is None:
        return result

    queue = deque() 
    queue.append(root)

    while queue:
        levelSise = len(queue) 

        for i in range(levelSise):
            currentNode = queue.popleft()

            if i == levelSise - 1:
                result.append(currentNode.val)
            
            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(15)
    print("Hi ",tree_right_view(root))

main()