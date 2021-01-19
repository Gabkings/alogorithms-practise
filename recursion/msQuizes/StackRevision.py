class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

    def __str__(self):
        return str(value)

class LinkedList:
    def __init__(self):
        self.head = None
        

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode.value
            currentNode = currentNode.next

    

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node
        return self.linkedList
    def pop(self):
        if self.isEmpty():
            return "No element to pop"
        node = self.linkedList.head
        self.linkedList.head = self.linkedList.head.next 
        return self.linkedList
    
    def peek(self):
        if self.isEmpty():
            return "Empty stack"
        return self.linkedList.head.value


sample = Stack()


sample.push(9)
sample.push(19)
sample.push(29)
sample.push(39)
print(sample)
s = sample.isEmpty()
print(s)
sample.pop()
print(sample)
print(sample.peek())