class LinkedList:

    def __init__(self, value):
        self.data = value
        self.next = None 

    @staticmethod
    def contructList(num_elements):
        head = None
        value = num_elements

        for i in range(num_elements):
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
        print("\n")
    
    @staticmethod
    def reverse(head):
        cur_node = head
        prev = None 
        while cur_node:
            new_node = cur_node.next 
            cur_node.next = prev 
            prev = cur_node
            cur_node = new_node
        return prev

    @staticmethod
    def k_reverse(head, k):
        if not head or k == 0:
            return head
        cur_node = head
        prev = None
        i = 0
        while cur_node and i < k:
            temp = cur_node.next 
            cur_node.next = prev 
            prev = cur_node
            cur_node = temp_node
            i += 1
        if(cur_node):
            head.next = LinkedList.k_reverse(head, k)

        return prev

    @staticmethod
    def find_kth_node_from_end1(head, k):
        length = 0
        n1 = head
        while n1:
            length += 1
            n1 = n1.next
        
        n1 = head 

        for i in range(1, length + 1):
            if (i == length - k + 1):
                return n1 
            n1 = n1.next
        return None 
    @staticmethod
    def find_kth_node_and_prev_node_from_begining(head, k):
        cur_node = head
        prev = None 
        i = 1

        while cur_node:
            if i == k:
                return cur_node, prev
            prev = cur_node
            cur_node = cur_node.next 
            i += 1
        return None
    
    @staticmethod
    def find_kth_node_and_prev_node_from_end(head, k):
        cur_node = head 
        length = 0
        prev = None
        i = 1
        while cur_node:
            length += 1
            cur_node = cur_node.next 
        cur_node = head

        while cur_node:
            if i == length - k + 1:
                return cur_node, prev 
            prev = cur_node
            cur_node = cur_node.next 
            i += 1
        return None

    @staticmethod
    def swap_neighbour(head, prev, n1, n2):
        n1.next = n2.next
        n2.next = n1
        if prev:
            prev.next = n2 
        else:
            head = n2 
        
        return head


    @staticmethod
    def swap_kth_node(head, k, length):
        if not head or k < 1 or k > length:
            return None 
        k1, prev1 = LinkedList.find_kth_node_and_prev_node_from_begining(head, k)
        k2, prev2 = LinkedList.find_kth_node_and_prev_node_from_end(head, k)

        if not k1 or not k2:
            return None
        
        if k1 == k2:
            return head 
        
        if k1.next == k2:
            return LinkedList.swap_neighbour(head, prev1, k1, k2)
        if k2.next == k1:
            return LinkedList.swap_neighbour(head, prev2, k2, k1)

        k1.next , k2.next = k2.next, k1.next 

        if(prev1):
            prev1.next = k2
        else:
            head = k2  
        if(prev2):
            prev2.next = k1 
        else:
            head = k1 
        
        return head

import sys 
def handle_error(): 
    print('Test failed')
    sys.exit(1)




MAX_NUM_ELEMENTS = 10

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range(MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        head = LinkedList.contructList(num_elems)

        #Passing k value of 0 should return in an error
        ret_val = LinkedList.swap_kth_node(head, 0, num_elems)
        if (ret_val):
            handle_error()

        #We test for different k values
        for k in range(1, num_elems + 1): 

            print('Size = {}, k = {}'.format(num_elems, k) )
            print('Input  : ', end='')
            LinkedList.display(head)

            #Swap the kth element
            head = LinkedList.swap_kth_node(head, k, num_elems)

            print('Output : ', end='')
            LinkedList.display(head)

            #Verify the result
            k_node, k_prev = LinkedList.find_kth_node_and_prev_node_from_begining(head, k)
            if (k_node.data != num_elems - k + 1):
                handle_error()

            #Again swap the kth element to get back the original linked list
            head = LinkedList.swap_kth_node(head, num_elems - k + 1, num_elems)

            #Verify the result
            k_node, k_prev = LinkedList.find_kth_node_and_prev_node_from_begining(head, k)
            if (k_node.data != k):
                handle_error()
    
            print('_______________________________________')

        #Passing a value of k that is greater than length of linked list should return an error
        ret_val = LinkedList.swap_kth_node(head, num_elems + 1, num_elems)

        if (ret_val):
            handle_error()


    print('Test passed')

            


