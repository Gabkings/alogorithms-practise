class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # avg O(log(n)) T, space = O(1)
    # worst O(n), space O(1) 
    def insert(self, value):
        currNode = self
        while True:
            if value < currNode.value:
                if currNode.left is None:
                    currNode.left = BST(value)
                    print("Inserted on the left")
                    break
                else:
                    currNode = currNode.left
            else:
                if currNode.right is None:
                    currNode.right = BST(value)
                    print("Inserted on the right")
                    break
                else:
                    currNode = currNode.right
        return self

    # avg O(log(n)) T, space = O(1)
    # worst O(n), space O(1) 
    def contains(self, value):
        currNode = self
        while currNode is not None:
            if value < currNode.value:
                currNode = currNode.left
            elif value > currNode.value:
                currNode = currNode.right
            else:
                return True
        return False

    def getMinValue(self):
        currNode = self
        while currNode is not None:
            currNode = currNode.left
        return currNode.value

    # avg O(log(n)) T, space = O(1)
    # worst O(n), space O(1) 
    def remove(self, value, pNode = None):
        currNode = self
        while currNode is not None:
            if value < currNode.value:
                pNode = currNode
                currNode = currNode.left
            elif value > currNode.value:
                pNode = currNode
                currNode = currNode.right
            else:
                if currNode.left is not None and currNode.right is not None:
                    currNode.value = currNode.right.getMinValue()
                    currNode.right.remove(currNode.value, currNode)
                elif pNode is None:
                    if currNode.left is not None:
                        currNode.value = currNode.left.value
                        currNode.left = currNode.left.left 
                        currNode.right = currNode.left.right 
                    elif currNode.right is not None:
                        currNode.value = currNode.right.value
                        currNode.right = currNode.right.right
                        currNode.left = currNode.right.left 
                elif pNode.left == currNode:
                    pNode.left = currNode.left if not None else currNode.right
                elif pNode.right == currNode:
                    pNode.right = currNode.left if not None else currNode.right
                break
        return self

    def validateBst(self):
        tree = self
        return self.validateBstHelper(tree, float("-inf"), float("inf"))
    
    def validateBstHelper(self, tree, minVal, maxVal):
        if tree is None:
            return True
        
        if tree.value < minVal or tree.value >= maxVal:
            return False
        leftIsValid = self.validateBstHelper(tree.left, minVal, tree.value)

        return leftIsValid and self.validateBstHelper(tree.right, tree.value, maxVal)

    def inOrderTraversal(self, root, arr):
        
        if root is not None:
            self.inOrderTraversal(root.left, arr)
            arr.append(root.value)
            self.inOrderTraversal(root.right, arr)
        return arr

    def preOrderTraversal(self,root, arr):
        if root is not None:
            arr.append(root.value)
            self.preOrderTraversal(root.left, arr)
            self.preOrderTraversal(root.right, arr)
        return arr

    def postOderTraversal(self,root, arr):
        if root is not None:
            self.postOderTraversal(root.left, arr)
            self.postOderTraversal(root.right, arr)
            arr.append(root.value)
        return arr
        



bst = BST(30)

bst.insert(20).insert(40).insert(50).insert(21).insert(10).insert(23)

ct = bst.contains(23)
vbst = bst.validateBst()
print(ct)
print(vbst)
print("In order traversal \n")
print(bst.inOrderTraversal(bst, arr = []))
print("Pre order traversal \n")
print(bst.preOrderTraversal(bst, arr = []))
print("Post order traversal \n")
print(bst.postOderTraversal(bst, arr = []))
print(vbst)