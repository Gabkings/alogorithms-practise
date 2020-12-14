from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currentnode = self.head
        while currentnode:
            yield currentnode
            currentnode = currentnode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return "->".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generateList(self, n , minV, maxV):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minV, maxV))
        return self

customList = LinkedList()

customList.generateList(10, 0 , 99)
# print(customList)
# print(customList.__len__())