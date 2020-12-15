class CircularQueue:
    # time complexity is o(n) because we are creting n elements 
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        # the queue is emepty if the top is equal to -1
        if self.top == -1:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            return "No empty space to insert items"
        else:
            # set the top value to start if there exist an element at last index
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                # increment the top position
                self.top += 1
                # check if we are inserting the first element
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "item inserted successfully"

    def dequeue(self):
        if self.isEmpty():
            return "No element to remove"
        else:
            firstElement = self.items[self.start]
            first = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[first] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "No elememts in the list"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1
        

sampleQueue = CircularQueue(4)

print(sampleQueue) 
print(sampleQueue.isFull())
print(sampleQueue.isEmpty())
print(sampleQueue.enqueue(3))
print(sampleQueue.enqueue(4))
print(sampleQueue.enqueue(5))
print(sampleQueue.enqueue(6))
print(sampleQueue)
print(sampleQueue.dequeue())
print(sampleQueue.dequeue())
print(sampleQueue.dequeue())
print(sampleQueue.dequeue())


print(sampleQueue)
