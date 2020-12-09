class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# creating a linked list
signlyList = SinglyLinkedList()

node1 = Node(1)
node2 = Node(2)

# assign the head to first node
signlyList.head = node1
signlyList.head.next = node2
signlyList.tail = node1