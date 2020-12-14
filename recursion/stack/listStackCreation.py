class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return self
        
    def pop(self):
        if self.isEmpty:
            return "No element to remove"
        else:
            return self.list.pop()
    
    def delete(self):
        self.list = None


    def peek(self):
        if self.isEmpty():
            return "List is empty"
        else:
            return self.list[len(self.list) -1]

sampleStack = Stack()
sampleStack.push(4)
sampleStack.push(5)
sampleStack.push(6)
print("this is peeek method")
print(sampleStack.peek())
print("This pop method")
print(sampleStack.pop())
print(sampleStack)
print("Deleting entire list")
print(sampleStack.delete())