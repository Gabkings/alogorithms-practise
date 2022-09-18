class LinkedList:
    def __init__(self, value):
        self.data = value
        self.next = None

    @staticmethod
    def constructList(num_elems):
        head = None 
        value = num_elems
        for i in range(num_elems):
            new_node = LinkedList(value)
            new_node.next = head 
            head = new_node
            value -= 1
        return head

    @staticmethod
    def display(head):
        cur_node = head 

        while cur_node:
            print("{}".format(cur_node.data), end="")
            cur_node = cur_node.next 

        


    @staticmethod
    def delete(node):
        if(node.next):
            node2 = node.next 
            node.data = node2.data 
            node.next = node2.next 
            return True 
        return False

import sys 
def handle_error(): 
    print('Test failed')
    sys.exit(1)
    


    



MAX_NUM_ELEMENTS = 10

import random

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range(2, MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 2, the linked list will be 1->2 
        head = LinkedList.constructList(num_elems)

        #Choose a random position to delete. It should not be the last element
        k = random.randint(0, num_elems - 2)

        print('Deleting {}th node '.format(k) )
        print('Input  : ', end='')
        LinkedList.display(head)

        #Find the node at position k
        cur_node = head
        for i in range(k): 
            cur_node = cur_node.next
    
        #delete the node
        ret_val = LinkedList.delete(cur_node)

        print(' Output  : ', end=' ')
        LinkedList.display(head)

        #Verify the result
        if (not ret_val):
            handle_error()

        print('_____________________________________________')



    print('Test passed')