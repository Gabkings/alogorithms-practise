class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next 

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)
    
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            return "No itmes in the queue"
        return self.linkedList.head.value
    
    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            node.next = self.linkedList.head
            self.linkedList.head = node
            self.linkedList.tail = node
            return "Enqueued"
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node
            return "Enqueued"

    def dequeue(self):
        if self.isEmpty():
            return "No element to dequeue"
        node = self.linkedList.head.value 
        self.linkedList.head = self.linkedList.head.next 
        return node
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


sample_q = Queue()

print(sample_q.isEmpty())
sample_q.enqueue(10)
print(sample_q.isEmpty())
print(sample_q.peek())
sample_q.enqueue(20)
sample_q.enqueue(30)
sample_q.enqueue(40)

print(sample_q)
sample_q.dequeue()
print(sample_q)