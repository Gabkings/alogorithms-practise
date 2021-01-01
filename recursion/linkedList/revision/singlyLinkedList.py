class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse(self):
        if self.start_node is None:
            print("No items to traverse through")
        
        n = self.start_node
        while n is not None:
            print(n.item , " ")
            n = n.ref

    def insert_at_begining(self, data):
        new_node = Node(data)

        new_node.ref = self.start_node
        self.start_node = new_node
        print("Node inserted at the begining")

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
        print("Node inserted at end successfully")

    def insert_after_node(self, x , data):
        if self.start_node is None:
            return "No node currently"
        new_node = Node(data)
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        new_node.ref = n.ref
        n.ref = new_node
        print("Node inserted after "+str(x)+" successfully")

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            print("Node inserted before "+str(x)+" Successful")

    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):
        if self.start_node is None:
            return 0
        count = 0
        n = self.start_node
        while n is not None:
            count += 1
            n = n.ref
        return count

    def search(self, x):
        if self.start_node is None:
            return False
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    return True
                    break
                n = n.ref
            return False

    def creatingList(self):
        nums = int(input("How nodes do you want to create"))

        for i in range(nums):
            value = int(input("Enter the node value to insert"))
            self.insert_at_end(value)

    def reverseList(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev

    
    


# singlyList = LinkedList()
# singlyList.traverse()
new_linked_list = LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_begining(20)
new_linked_list.insert_after_node(10, 17)
new_linked_list.insert_before_item(17, 25)
new_linked_list.traverse()
print("Counting the elements")
print(new_linked_list.get_count())

print("Searching for a item")
print(new_linked_list.search(30))
print("Creating a list")
new_linked_list.creatingList()
new_linked_list.traverse()
print(new_linked_list.get_count())