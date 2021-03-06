# from ..queues.linkedListQueue import Queue

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

class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None



bst = BinarySearchTree(70)

def insertNode(rootNode, nodeValue):
    if rootNode is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Node inserted ssuccess"

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.data) 
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)
def inOrderTraversal(rootNode):
    if rootNode is None:
        return 
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        return "Value is found on the rootNode"
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            return "The value is found on the left"
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            return "Node is found on the right"
        else:
            searchNode(rootNode.rightChild, nodeValue)
    return "node does not exist"

def minimumNode(rootNode):
    current = rootNode
    while(current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return
    if nodeValue < rootNode.data:
        rootNode = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode = deleteNode(rootNode.rightChild, nodeValue)
    else:
        # deleting a node with one child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # deleting the node  with two children
        temp = minimumNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) 
    return rootNode

def deleteEntire(rootNode): 
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BT deleted"

print(insertNode(bst, 50))
print(insertNode(bst, 20))
print(insertNode(bst, 30))
print(insertNode(bst, 40))
print(insertNode(bst, 60))
print(insertNode(bst, 80))
print("postal order traversal")
postOrderTraversal(bst)
print("Pre-order traversal")
preOrderTraversal(bst)

print("In order traversal")
inOrderTraversal(bst)
print("Level order traversal")
levelOrderTraversal(bst)
print("searching for a node")
print(searchNode(bst, 80))
print("Deleting the node")
deleteNode(bst, 20)
print("Level order traversal after delete")
levelOrderTraversal(bst)
print(deleteEntire(bst))


