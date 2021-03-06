class MyQueue:
    
    def __init__(self):
        self.stack = []
        self.reversed = []
        self.first = None

    def __str__(self):
        values = [str(x) for x in self.stack]
        return " ".join(values)

    def push(self, element):
        if not self.stack:
            self.first = element
        self.stack.append(element)

    def pop(self):
        if not self.reversed:
            while self.stack:
                self.reversed.append(self.stack.pop())
        return self.reversed.pop()
        
    def top(self):
        if self.reversed:
            return self.reversed[-1]
        return self.first 
        
    def emepty(self):
        return not self.stack and not self.reversed

sampleQ = MyQueue()

sampleQ.push(2)
sampleQ.push(3)
sampleQ.push(4)
sampleQ.push(5)


print(sampleQ.top())
print(sampleQ.pop())
print(sampleQ.top())
print(sampleQ)