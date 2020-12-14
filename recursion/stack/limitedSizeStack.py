class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def push(self, value):
        if len(self.list) == self.maxSize:
            return "List is full"
        self.list.append(value)

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False

    def isEmpty(self):
        if self.list ==[]:
            return True
        return False
    
    def pop(self):
        if self.isEmpty:
            return "No element to remove"
        return self.list.pop()
    
    def peek(self):
        if self.list is not self.isEmpty():
            return self.list[len(self.list) -1]
        return "No element available"

    def delete(self):
        self.list = None


sampleStack = Stack(6)
sampleStack.push(8)
sampleStack.push(5)
sampleStack.push(7)
sampleStack.push(9)
sampleStack.push(2)
sampleStack.push(1)
# print(sampleStack)
print(sampleStack.peek())
print(sampleStack.isFull())
print(sampleStack.isEmpty())
print(sampleStack.delete())
print(sampleStack.isEmpty())
