class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinks:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createNode(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "Node Created successfully"

    def insertDLL(self, value, location):
        if self.head is None:
            print("List does not exist")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode 

            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    
                    
                

doublyLL = DoubleLinks()
doublyLL.createNode(3) 
doublyLL.insertDLL(3,0)
doublyLL.insertDLL(4,0)
doublyLL.insertDLL(5,1)
doublyLL.insertDLL(6,0)
doublyLL.insertDLL(7,1)
print(print([node.value for node in doublyLL]))