
import random

MAX_NUM_ELEMENTS = 10
MAX_VALUE = 10
class LinkedList:

    def __init__(self, value=0):
        self.data = value
        self.next = None 

    @staticmethod
    def display(head):
        cur_node = head 
        while cur_node:
            print("{}".format(cur_node.data), end="")
            cur_node = cur_node.next

    
    @staticmethod
    def handle_error(): 
        print('Test failed')
        sys.exit(1)

    
    @staticmethod
    def construct(num_elemes):
        head = None 
        value = num_elemes
        for i in range(num_elemes):
            new_node = LinkedList(value)
            new_node.next = head
            head = new_node 
            value -= 1
        return head 

    @staticmethod
    def constructList(num_elements):
        head = None
        for i in range (num_elements):
            new_node = LinkedList()
            new_node.data = random.randint(0, MAX_VALUE - 1)
            new_node.next = head
            head = new_node
        return head

    @staticmethod
    def remove_duplicates(head):
        if not head or not head.next:
            return 
        
        cur_node = head
        while cur_node:
            iter_node = cur_node.next 
            prev_node = cur_node
            while iter_node:
                if(iter_node.data == cur_node.data):
                    prev_node.next = iter_node.next 
                    iter_node = iter_node.next 
                else:
                    prev_node = iter_node
                    iter_node = iter_node.next 
            cur_node = cur_node.next 
    
    @staticmethod
    def verify(head): 
        if not head or not head.next:
            return 
        
        cur_node = head

        while cur_node:
            iter_node = cur_node.next 

            while iter_node:
                if cur_node.data == iter_node.data:
                    handle_error()
                iter_node = iter_node.next 

            cur_node = cur_node.next


if (__name__ == '__main__'):
    
    #Test for different linked list lengths:
    for num_elems in range (MAX_NUM_ELEMENTS + 1) :
        #Construct a linked list with random elements. The linked list can contain duplicates
        head = LinkedList.constructList(num_elems)

        print('Input  : ', end='')
        LinkedList.display(head)

        #Remove the duplicates
        LinkedList.remove_duplicates(head)

        print(' Output : ', end='')
        LinkedList.display(head)

        #Verify the linked list
        LinkedList.verify(head)

        print('__________________________________________________________')


    print('Test passed ')




    