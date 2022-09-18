class LinkedNode(object):
    def __init__(self, val):
        self.data = val 
        self.next = None 

    @staticmethod
    def reverse(head):
        cur_node = head

        prev_node = None

        while cur_node:
            next_node = cur_node.next 
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node

    @staticmethod
    def k_reverse(head, k):
        if not head or k == 0:
            return head
        cur_node = head
        prev_node = None
        i = 0
        while cur_node and i < k:
            temp_node = cur_node.next 
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp_node 
            i += 1
        if cur_node:
            head.next = LinkedNode.k_reverse(cur_node, k)
        return prev_node 

    @staticmethod
    def find_kth_node_from_end(head, k):
        length = 0
        n1 = head 
        while n1:
            length += 1
            n1 = n1.next 
        n1 = head
        
        for i in range(1, length + 1):
            if(i == length -k + 1):
                return n1 
            ni = n1.next 
        return None 
        



    @staticmethod
    def contructList(num_elements):
        head = None 
        value = num_elements
        for i in range(num_elements):
            new_node = LinkedNode(value)
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
        print("")


MAX_NUM_ELEMENTS_IN_LIST = 10
MAX_NUM_ELEMENTS = 10

k = 2
import sys
def handle_error(): 
    print('Test failed')
    sys.exit(1)
def test_reverse(reverse_fn):

    #Test Non-Recursive Linked List Reversal
    #We test for different linked list lengths ranging from 0 to MAX_NUM_ELEMENTS_IN_LIST
    for num_elems in range(MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 1, the linked list will be 1->NULL
        #If num_elems = 2, the linked list will be 1->2->NULL
        head = LinkedNode.contructList(num_elems)

        # print('Input  : ', end='')
        # LinkedNode.display(head)

        # head = reverse_fn(head)

        # print('Output : ', end='')
        # LinkedNode.display(head)

        #Iterate the reversed linked list and check if it is in reverse order
        # cur_node = head
        # for j in range(num_elems): 
        #     if (cur_node.data != num_elems - j): 
        #         handle_error()
        
        #     cur_node = cur_node.next
    
        # print('_______________________________________________')

       

MAX_NUM_ELEMENTS = 10

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range(MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        head = LinkedNode.contructList(num_elems)

        #Passing k value of 0 should return in an error
        ret_val = LinkedNode.swap_kth_node(head, 0, num_elems)
        if (ret_val):
            handle_error()

        #We test for different k values
        for k in range(1, num_elems + 1): 

            print('Size = {}, k = {}'.format(num_elems, k) )
            print('Input  : ', end='')
            LinkedNode.display(head)

            #Swap the kth element
            head = LinkedNode.swap_kth_node(head, k, num_elems)

            print('Output : ', end='')
            LinkedNode.display(head)

            #Verify the result
            k_node, k_prev = LinkedNode.find_kth_node_from_begin(head, k)
            if (k_node.data != num_elems - k + 1):
                handle_error()

            #Again swap the kth element to get back the original linked list
            head = LinkedNode.swap_kth_node(head, num_elems - k + 1, num_elems)

            #Verify the result
            k_node, k_prev = LinkedNode.find_kth_node_from_begin(head, k)
            if (k_node.data != k):
                handle_error()
    
            print('_______________________________________')

        #Passing a value of k that is greater than length of linked list should return an error
        ret_val = LinkedNode.swap_kth_node(head, num_elems + 1, num_elems)

        if (ret_val):
            handle_error()


    print('Test passed')