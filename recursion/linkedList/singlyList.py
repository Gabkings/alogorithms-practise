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

    # traversing SLL
    def traverseSLL(self):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next

    # searching an item in the list
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("List does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "node does not exist"

    # deleting the node
    def deletingNodeSSL(self, location):
        if self.head is None:
            print("List does not exist")
        else:
            if location == 0:
                # check if only 1 node exist
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head

                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index  += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


    # deleting the entire list
    def deleteEntireList(self):
        if self.head is None:
            print("List does not exist")
        else:
            self.head = None
            self.head = None


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
signlyList.insertSLL(9,1)

print([node.value for node in signlyList])


# searching for a value
print(signlyList.searchSLL(1))

print(signlyList.deletingNodeSSL(1))

print("----")
print(signlyList.traverseSLL())