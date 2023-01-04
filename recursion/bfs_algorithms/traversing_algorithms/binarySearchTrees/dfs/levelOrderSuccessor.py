class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left, self.right = None, None 

from collections import deque

def find_successor(root, key):
    if root is None:
        return None

    queue = deque() 

    queue.append(root)
    while queue:
        currentNode = queue.popleft() 

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right) 

        if currentNode.val == key:
            break 

    return queue[0].val if queue else None

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(15)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(11)
    print("Hi ",find_successor(root, 10))

main()

    