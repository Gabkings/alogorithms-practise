class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next


class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
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
            return "No node to delete"
        nodeValue = self.linkedList.head.value
        self.linkedList.head = self.linkedList.head.next
        return nodeValue

    def peek(self):
        if self.isEmpty():
            return "No node to display"
        nodeValue = self.linkedList.head.value
        return nodeValue  



    


sampleStack = Stack()
sampleStack.push(2)
sampleStack.push(1)
sampleStack.push(3)
sampleStack.push(4)
print(sampleStack)
print(sampleStack.isEmpty())

print(sampleStack.peek())
print(sampleStack.pop())
print(sampleStack.peek())