class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL:
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

    def createLinkedList(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        print("Node created successfully")

    def insertNewNode(self,value, location):
        if self.head is None:
            print("List does not exist")
        else:
            node = Node(value) 
            if location == 0:
                node.prev = self.tail
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.tail.next = node
            
            elif location == 1:
                node.next = self.head
                node.prev = self.tail
                self.head.prev = node
                self.tail.next = node
                self.tail = node

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                node.next = tempNode.next
                node.prev = tempNode
                node.next.prev = node
                tempNode.next = node
    
    # traversing circular double linked list
    def traversingCDLL(self):
        if self.head is None:
            print("List does not exist")
        else:
            tempNome = self.head
            while tempNome:
                print(tempNome.value)
                if tempNome == self.tail:
                    break
                tempNome = tempNome.next
    
    # traversing backwords
    def traversingCDLLBackword(self):
        if self.head is None:
            print("Linked does not exist")
        else:
            tempNode = self.tail 
            while tempNode :
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchValue(self, value):
        if self.head is None:
            print("List does not exist")

        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                if tempNode == self.tail:
                    return "Node does not exist"
                
                tempNode = tempNode.next 
                
    def deletingNodeAtSpecificLocation(self, location):
        if self.head is None:
            print("List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: 
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode


    def deleteCDLL(self):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            self.tail.next = None
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("List has been deleted")


circularDLL = CircularDLL()
circularDLL.createLinkedList(3)

circularDLL.insertNewNode(2,0)
circularDLL.insertNewNode(4,1)
circularDLL.insertNewNode(5,2)

print([node.value for node in circularDLL])
circularDLL.traversingCDLL()

print([node.value for node in circularDLL])
circularDLL.traversingCDLLBackword()

print([node.value for node in circularDLL])
print(circularDLL.searchValue(5))


print(circularDLL.deletingNodeAtSpecificLocation(2))
print([node.value for node in circularDLL])

print(circularDLL.deleteCDLL())
print([node.value for node in circularDLL])