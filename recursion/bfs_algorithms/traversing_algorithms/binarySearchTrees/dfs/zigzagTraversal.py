from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left, self.right = None, None

def zigzagTraversal(root):
    result = []

    if root is None:
        return result 

    queue = deque()
    queue.append(root)
    leftToRight = True 
    while queue:
        levelSise = len(queue)
        currentLevel = deque()
        for _ in range(levelSise):
            currentNode = queue.popleft()
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)       
        result.append(list(currentLevel))
        leftToRight = not leftToRight

    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(15)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(11)
    print("Hi ",zigzagTraversal(root))

main()