class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    # def insert_at_start(self, data):
    #     node = Node(data)
    #     if self.head is None:
    #         self.head = node
    #         self.tail = node
    #     else:
    #         node.next = self.head
    #         self.head = node


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

    def enqueue(self, data):
        node = Node(data)
        if self.linkedList.head is None:
            node.next = self.linkedList.head
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node 

    def dequeue(self):
        if self.isEmpty():
            return 
        node = self.linkedList.head
        self.linkedList.head = self.linkedList.head.next 
        return node.data



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None 
    



newBT = TreeNode("Drinks")
cold = TreeNode("Cold")    
hot = TreeNode("Hot")
newBT.leftChild = cold
newBT.rightChild = hot

def preOrderTraversal(rootNode):
    if rootNode is not None:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(newBT)

def inOrderTraversal(rootNode):
    if rootNode is not None:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data) 
        inOrderTraversal(rootNode.rightChild)
# inOrderTraversal(newBT)

def postOrderTraversal(rootNode):
    if rootNode is not None:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

# postOrderTraversal(newBT)


def levelOrderTraversal(rootNode):
    if rootNode is not None:
        customQ = Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            print(root.data)
            if root.leftChild is not None:
                customQ.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQ.enqueue(root.rightChild)

# levelOrderTraversal(newBT)

def searchBT(rootNode, node):
    if rootNode is not None:
        customQ = Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.data == node:
                print(root.data)
                return "OK"
            if root.leftChild is not None:
                customQ.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQ.enqueue(root.rightChild)
        print("Not found")
        return "Not found"
# searchBT(newBT, "Hot")

def insertNode(rootNode, node):
    if not rootNode:
        rootNode = node
    else:
        customQ = Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.leftChild is not None:
                customQ.enqueue(root.leftChild)
            else:
                print("Inserted at left")
                root.leftChild = node
                return
            if root.rightChild is not None:
                customQ.enqueue(root.rightChild)
            else:
                root.rightChild = node
                print("Inserted at right")
                return

def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)

        return root.data


# insertNode(newBT, "Colla")
# insertNode(newBT, "Coffee")
# insertNode(newBT, "Spirit")

print("Deepest node") 
s = getDeepestNode(newBT)
print(s)

def deletingDepestNode(rootNode, dNode):
    if rootNode is not None:
        customQ = Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.data == dNode:
                root = None
                return "Deleted"
            if root.leftChild:
                if root.leftChild.data is dNode:
                    root.leftChild = None
                    return "Deleted from left"
                else:
                    customQ.enqueue(root.leftChild)
            if root.rightChild:
                if root.rightChild.data is dNode:
                    root.rightChild = None 
                    return "Deleted from right"
                else:
                    customQ.enqueue(root.rightChild)

s = getDeepestNode(newBT)

# d = deletingDepestNode(newBT, s)
# print(d)

def deteleNode(rootNode, node):
    if rootNode is not None:
        customQ = Queue()
        customQ.enqueue(rootNode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root = dNode
                deletingDepestNode(rootNode, dNode)
                return "Deleted"
            if root.leftChild is not None:
                customQ.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQ.enqueue(root.rightChild)
        return "Failed"

dd = deteleNode(newBT, "Hot")
print(dd)