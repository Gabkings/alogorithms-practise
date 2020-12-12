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
                


                

                    



circularDLL = CircularDLL()
circularDLL.createLinkedList(3)

circularDLL.insertNewNode(2,0)
circularDLL.insertNewNode(4,1)
circularDLL.insertNewNode(5,2)
print([node.value for node in circularDLL])
