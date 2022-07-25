class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # allocate the new node and put in the data
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("prev node must be in linked list")
            return 
        # allocate the new node and put in the data
        new_node = Node(new_data)

        new_node.next = prev_node.next 
        prev_node.next = new_node

    def append(self, new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 

        last = self.head
        while last.next:
            last = last.next 

        last.next = new_node
        return

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                temp = None
                return

        # search for the key to be deleted and keep track of prev node

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next 

        
        if temp is None:
            return 

        prev.next = temp.next
        temp = None

        return

    def getCount(self):
        count = 0

        temp = self.head

        while temp:
            count += 1
            temp = temp.next 
        
        return count

    def detectLoop(self):
        temp = self.head

        s = set()

        while temp:
            if(temp in s):
                return True
            
            s.add(temp)

            temp = temp.next

        return False

    def detectLoop2(self):
        slow_p = self.head

        fast_p = self.head

        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if(slow_p == fast_p):
                return True
        return False

    def reverse(self):
        prev = None 
        current = self.head
        while current is not None:
            next = current.next 
            current.next = prev
            prev = current
            current = next

        self.head = prev





def getIntersectionNode1(head1, head2):
    while head2:
        temp = head1

        while temp:

            if(temp == head2):
                return head2.data

            temp = temp.next
        head2 = head2.next 

    return None

def getIntersectionNode2(head1, head2):
    ptr1 = head1
    ptr2 = head2

    if ptr1 is None or ptr2 is None:
        return None
    
    while ptr1 != ptr2:
        ptr1 = ptr1.next 
        ptr2 = ptr2.next 

        if(ptr1 == ptr2):
            return ptr1.data 
        
        if(ptr1 == None):
            ptr1 = head2
        
        if(ptr2 == None):
            ptr2 = head1

    return ptr1

def push(head_ref, new_data):
    '''allacate the node and put in data'''
    new_node = Node(new_data)

    ''' link the old list of the new node'''
    new_node.next = (head_ref)

    '''move the head to point to new node'''

    (head_ref) = new_node
    return head_ref

def sortIntersectionList(a, b):
    dummy = Node(0)
    tail = dummy
    dummy.next = None

    while(a != None and b != None):
        if(a.data == b.data):
            tail.next = push((tail.next), a.data)
            tail = tail.next
            a = a.next 
            b = b.next 
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
    return (dummy.next)

def printList(node):
    while (node != None):
        print(node.data, end=' ')
        node = node.next;






llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth

llist.push(5)
# llist.insertAfter(third.next, 7)
# llist.insertAfter(second, 7)
llist.append(8)
llist.append(9)
llist.append(10)

print("Intial list")
llist.printList()

llist.reverse()
print("reversed")
llist.printList()

# llist.deleteNode(9)
# llist.deleteNode(8)

# newNode = Node(10)
# head1 = newNode
# newNode = Node(3)
# head2 = newNode
# newNode = Node(6)
# head2.next = newNode
# newNode = Node(9)
# head2.next.next = newNode
# newNode = Node(15)
# head1.next = newNode
# head2.next.next.next = newNode
# newNode = Node(30)
# head1.next.next = newNode

# llist.printList()

# count = llist.getCount()
# print("Counting elements")
# print(count)

# print("Detecting a loop")
# print(llist.detectLoop2())

# a = None;
# b = None;
# intersect = None;

# ''' Let us create the first sorted
#     linked list to test the functions
#     Created linked list will be
#     1.2.3.4.5.6 '''
# a = push(a, 6);
# a = push(a, 5);
# a = push(a, 4);
# a = push(a, 3);
# a = push(a, 2);
# a = push(a, 1);

# ''' Let us create the second sorted linked list
# Created linked list will be 2.4.6.8 '''
# b = push(b, 8);
# b = push(b, 6);
# b = push(b, 4);
# b = push(b, 2);

# ''' Find the intersection two linked lists '''
# intersect = sortIntersectionList(a, b);

# print("Linked list containing common items of a & b ");

# printList(intersect);

# print(getIntersectionNode2(head1, head2))
