
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def enqueue(self, item):
        self.items.append(item)
        return "Items add successfully"

    def dequeue(self):
        if self.isEmpty():
            return "No item to remove"
        # remove the first element
        self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "No items in the list"
        item = self.items[0]
        return item

    def delete(self):
        self.items = None
        

sampleQueue = Queue()



sampleQueue.enqueue(2)
sampleQueue.enqueue(3)
sampleQueue.enqueue(4)
sampleQueue.enqueue(5)
print(sampleQueue)

print("check if list is empty")
print(sampleQueue.peek())
print("removing element")
sampleQueue.dequeue()
print(sampleQueue)
print(sampleQueue.isEmpty())
