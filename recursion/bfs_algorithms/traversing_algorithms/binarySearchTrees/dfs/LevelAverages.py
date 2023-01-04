class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left, self.right = None, None 

from collections import deque
def levelAverages(root):
    result = []

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        runningSum = 0

        for _ in range(levelSize): 
            currentNode = queue.popleft()
            runningSum += currentNode.val 

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)
        
        result.append(runningSum / levelSize)

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
    print("Hi ",levelAverages(root))

main()


