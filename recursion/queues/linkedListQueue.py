class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        head = self.head
        while head:
            yield head
            head = head.next
    
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return " ".join(values)

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False


    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node
        return self.linkedList.head

    def dequeue(self):
        if self.isEmpty():
            return "No element to remove"
        else:
            tempNode = self.linkedList.head.value
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "No element to display"
        else:
            return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
            


sampleQueue = Queue()

print(sampleQueue.isEmpty())

print(sampleQueue)
print(sampleQueue.enqueue(2))
print(sampleQueue.enqueue(3))
print(sampleQueue.enqueue(4))
print(sampleQueue.enqueue(5))
print(sampleQueue.enqueue(6))
print(sampleQueue)
print(sampleQueue.dequeue())
print(sampleQueue.dequeue())
print(sampleQueue)
print(sampleQueue.peek())