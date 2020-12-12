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

    def traverseDLL(self):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # search for a value
    def searchValue(self, value):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    print(tempNode.value)
                tempNode = tempNode.next
            return "Node does not exist"
    def reverseTraversal(self):
        if self.head is None:
            print("No list exist")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # deleting a single node
    def deleteDLL(self, location):
        if self.head is None:
            print("List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNone = self.head
                index = 0
                while index < location -1:
                    tempNone = tempNone.next
                    index += 1
                tempNone.next = tempNone.next.next
                tempNone.next.prev = tempNone

    def deleteEntireDLL(self):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("DLL has been deleted")


doublyLL = DoubleLinks()
doublyLL.createNode(3) 
doublyLL.insertDLL(3,0)
doublyLL.insertDLL(4,0)
doublyLL.insertDLL(5,1)
doublyLL.insertDLL(6,0)
doublyLL.insertDLL(7,1)
print(print([node.value for node in doublyLL]))

doublyLL.searchValue(9)

print(doublyLL.traverseDLL())
print(doublyLL.reverseTraversal())

doublyLL.deleteDLL(2) #deleting a node at index 2
doublyLL.deleteDLL(1) #deleting last node
doublyLL.deleteDLL(0) #deleting first node
print(print([node.value for node in doublyLL]))

doublyLL.deleteEntireDLL()

print(print([node.value for node in doublyLL]))