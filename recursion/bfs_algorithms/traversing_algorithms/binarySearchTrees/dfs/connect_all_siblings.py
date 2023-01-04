from __future__ import print_function
class TreeNode:

    def __init__(self, val):

        self.val = val 
        self.left, self.right, self.next = None, None, None 

    def print_tree(self):
        print("Traversing using the next pointer ", end='')
        current = self 
        while current:
            print(str(current.val) +" ", end='')
            current = current.next





from collections import deque
def connect_all_siblings(root):
    if root is None:
        return

    queue = deque() 
    queue.append(root)
    currentNode, previousNode = None, None 

    while queue:
        currentNode = queue.popleft() 
        if previousNode:
            previousNode.next = currentNode
            previousNode = currentNode 

        if currentNode.left:
            queue.append(currentNode.left)

        if currentNode.right:
            queue.append(currentNode.right)



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Hi ",connect_all_siblings(root))
    root.print_tree()

main()
