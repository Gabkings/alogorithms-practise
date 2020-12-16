class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ", "+str(self.next)
        return string

class MinimumStack():
    def __init__(self):
        self.top = None
        self.minMum = None

    def min(self):
        if not self.minMum:
            return None
        return self.minMum.value
    
    def push(self, item):
        if self.minMum and (self.minMum.value < item):
            self.minMum = Node(value=self.minMum.value, next=self.minMum)
        else:
            self.minMum = Node(value = item, next= self.minMum)
        self.top = Node(value = item, next = self.top)