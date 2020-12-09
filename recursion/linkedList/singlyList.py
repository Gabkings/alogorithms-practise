class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # iterable helper 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # inserting nodes at begining, middle and last
    def insertSLL(self, value, location):
        newNode = Node(value)
        # creating the node
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            # inserting at the begininig
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            # inserting at the last
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # inserting at the middle
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

# creating a linked list
signlyList = SinglyLinkedList()
# insert at first 
signlyList.insertSLL(1,0)
# insert at the last
signlyList.insertSLL(2,1)
signlyList.insertSLL(4,1)
signlyList.insertSLL(1,1)
signlyList.insertSLL(5,0)
# insert at the middle
signlyList.insertSLL(6,3)
signlyList.insertSLL(0,0)

print([node.value for node in signlyList])