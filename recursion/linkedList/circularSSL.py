class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            

    # inserting a node
    def createCircularSSL(self,item):
        node = Node(item)
        node.next = node
        self.head = node
        self.tail = node
        return "New node has been created"

    # inserting 
    def insertCSLL(self,value,location):
        if self.head is None:
            print("Head does not exist")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverseCSLL(self):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchNode(self, nodeValue):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "Node does not exist"
                    break

    # deleting
    def deleteNode(self, location):
        if self.head is None:
            print("List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode == self.tail.next:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

            



circularSSL = CircularSLL()
circularSSL.createCircularSSL(12)
circularSSL.insertCSLL(2,0)
circularSSL.insertCSLL(4,1)
circularSSL.insertCSLL(5,2)

circularSSL.insertCSLL(9,2)
circularSSL.insertCSLL(7,2)
circularSSL.insertCSLL(8,2)

print([node.value for node in circularSSL])
print(circularSSL.traverseCSLL())
# searching
print("Searching node")
circularSSL.searchNode(9)

# circularSSL.deleteNode(0)

print([node.value for node in circularSSL])
circularSSL.deleteNode(1)

print([node.value for node in circularSSL])