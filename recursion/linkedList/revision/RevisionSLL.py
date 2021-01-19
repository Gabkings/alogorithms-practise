class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None 
    
    def __str__(self):
        return str(self.value)

class SSL: 
    def __init__(self):
        self.head = None
        self.tail = None 

    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return "->".join(values)

    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        print("Creation successful")

    def traverse(self):
        if self.head is None:
            return "Empty list"
        current = self.head 
        while current is not None:
            print(current.value)
            current = current.next 

    def searchValue(self, val):
        if self.head is None:
            return "No value to search"
        current = self.head

        while current is not None:
            if current.value == val:
                return current.value
            current = current.next
        return -1

    def insert(self, value , location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        if location == 0:
            newNode.next = self.head
            self.head = newNode 

        elif location == 1:
            current = self.head
            while current is not None:
                current = current.next
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
        else:
            index = 0
            current = self.head
            while index < location-1:
                current = current.next
                index += 1
            nextNode = current.next
            current.next = newNode
            newNode.next = nextNode

    def delete(self, location):
        if self.head is None:
            return "Empty list"

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current is not None:
                    if current.next == self.tail:
                        break
                    current = current.next
                current.next = None
                self.tail = current
        else:
            index = 0
            current = self.head
            while index < location -1:
                current = current.next
                index += 1
            nextNode = current.next
            current.next = nextNode.next

    def insertAfterNode(self, node, value):
        if self.head is None:
            return "No nodes currently"
        new_node = Node(value)
        current = self.head
        while current is not None:
            if current.value == node:
                break 
            current = current.next
        new_node.next = current.next
        current.next = new_node
        print("Node inserted successfully after "+str(node))

    def insertBeforeNode(self, node , data):
        if self.head is None:
            return "List is empty"
        newNode = Node(data)
        if self.head.value == node:
            newNode.next = self.head
            self.head = newNode
            return "Insertion successfull"
        
        curr = self.head
        while curr.next is not None:
            if curr.next.value == node:
                break
            curr = curr.next
        if curr.next is None:
            print("node does not exist")
            return
        else:
            newNode.next = curr.next
            curr.next = newNode
            print("Success")
            return
    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
            print("Insertion successful")
            return
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            i += 1
            n = n.next

        if n is None:
            print("Index out of bound")
        else:
            new_node.next = n.next
            n.next = new_node
            print("Insertion successful")
            return
            
    def reverse(self):
        prev = None 
        start = self.head
        while start is not None:
            curr = start.next
            start.next = prev
            prev = start
            start = curr
        self.head = prev

    def get_count(self):
        if self.head is None:
            return 0
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.next
        return count

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    def delete_at_start(self):
        if self.head is None:
            print("The list is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("No element to delete")
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def delete_by_value(self, node):
        if self.head is None:
            print("Node node to delete")
            return

        if self.head.value == node:
            self.head = self.head.next

        n = self.head 
        while n is not None:
            if n.next.value == node:
                break
            n = n.next
        if n.next is None:
            print("Index out of bound")
            return
        n.next = n.next.next 
        return

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail


def remove_dublicates(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.next.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next 
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next 
        return ll

def remove_dublicates_without_buffer(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head 
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.next.value == currentNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next 
        return ll

def nthToTheLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head 

    # move pointer2 to the n
    for i in range(n):
        if pointer2 is None:
            return None 
        pointer2 = pointer2.next 
    # move the two pointer togeter
    while pointer2:
        pointer1 = pointer1.next 
        pointer2 = pointer2.next 
    return pointer1

def partion(ll, n):
    currNode = ll.head 
    ll.tail = ll.head 
    while currNode:
        nextNode = currNode.next 
        currNode.next = None
        if currNode.value < n:
            currNode.next = ll.head 
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode
    if ll.tail.next is not None:
        ll.tail.next = None

    return ll

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = SSL()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    # if carry != 0:
    #     ll.add(int(carry))
    return ll



ssl = SSL()
ssl.create(10)
ssl.insert(11,0)
ssl.insert(12,1)
ssl.insert(9,2)
ssl.insert(9,2)
ssl.insert(9,2)
ssl.insert(13,4)
ssl.insert(14,3)
ssl.insert(14,3)
ssl.insert(14,3)
ssl.insert(16,4)
ssl.insert(15,2)
# print("inserting after")
# ssl.insert_at_index(3, 88)
# ssl.traverse()
# print("Searching nodes")
# print(ssl.searchValue(9))

# print("deliting nodes")

# ssl.delete(1)
# ssl.traverse()

# ssl.reverse()
# print("Reversed list")
# ssl.traverse()

# print("Counting the elements")
# print(ssl.get_count())
# print("Inserting at end")
# ssl.insert_at_end(99)
# ssl.traverse()
# print("Deleting node at end")
# ssl.delete_by_value(88)
# ssl.traverse()

s = remove_dublicates_without_buffer(ssl)
print(s)

a = partion(ssl, 12)
print(a)

llA = SSL()
llB = SSL()

llA.insert_at_end(2)
llA.insert_at_end(9)
llA.insert_at_end(4)

llB.insert_at_end(4)
llB.insert_at_end(3)
llB.insert_at_end(7)
print("summing lists")
a = sumList(llA,llB)
print(llA)
print(llB)
print(a)