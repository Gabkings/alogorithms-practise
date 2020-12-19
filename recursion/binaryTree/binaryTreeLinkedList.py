class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        head = self.head
        while head:
            yield head
            head = head.next
    
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False


    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    def dequeue(self):
        if self.isEmpty():
            return "No element to remove"
        else:
            tempNode = self.linkedList.head.value
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "No element to display"
        else:
            return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# O(1) time complexit and space complexity
tree = TreeNode("Drinks")

leftChild = TreeNode("Cold")
rightChild = TreeNode("Hot")
coffe = TreeNode("Coffee")
tea = TreeNode("Tea")
cola = TreeNode("Colla")
sprit = TreeNode("Spirit")
tree.leftChild = leftChild
tree.rightChild = rightChild
rightChild.rightChild= coffe
rightChild.leftChild = tea
leftChild.rightChild = sprit
leftChild.leftChild = cola

# o(n) complexity and space complexity is o(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
print("pre-order traversal")
preOrderTraversal(tree)

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)

print("Inorder traversal")
inorderTraversal(tree)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

print("Post order tree traversal")
postOrderTraversal(tree)

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)

print("Level Order traversal")
levelOrderTraversal(tree)

def searchBT(rootNode, nodeValue):
    if rootNode is None:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == nodeValue:
                return root.data 
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "Not found"

print("Searching binary tree")
print(searchBT(tree, "Colla"))

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not( customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            else:
                root.leftChild = newNode
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)
                return "Inserted on left child successful"
            else:
                root.rightChild = newNode
                return "Inserted on right child successful"

print("Inserting a node")
print(insertNode(tree, "porridge"))