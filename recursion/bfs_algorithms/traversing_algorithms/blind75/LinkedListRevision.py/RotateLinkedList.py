class LinkedList:

    def __init__(self, value):
        self.data = value
        self.next = None 


    @staticmethod
    def display(head):
        cur_node = head
        while cur_node:
            print("{}".format(cur_node.data), end="")
            cur_node = cur_node.next 

    @staticmethod
    def construct(num_elems):
        head = None
        value = num_elems
        
        for i in range(num_elems):
            new_node = LinkedList(value)
            new_node.next = head 
            head = new_node
            value -= 1

        return head 







    @staticmethod
    def get_nth_node_from_end(head, k, length):
        cur_node = head
        prev = None 

        for i in range(1, length + 1):
            if (i == length - k + 1):
                return cur_node, prev 

            prev = cur_node
            cur_node = cur_node.next 
    

        return None, None

    @staticmethod
    def rotate(head, k, length):
        if length < 2:
            return head

        #shift times 
        k = k % length

        if k == 0:
            return head
        
        pivot, prev = LinkedList.get_nth_node_from_end(head, k, length)
        last = pivot 
        while last.next:
            last = last.next 
        
        last.next = head 
        prev.next = None 

        return pivot 

    
    @staticmethod
    def compare( head,  expected_result,  length):
        cur_node = head
    
        for i in range(length):
            if (not cur_node):
                handle_error()

            if (cur_node.data != expected_result[i]) :
                handle_error()
        
            cur_node = cur_node.next 
        

        if (cur_node):
            handle_error()

        

def perform_test( head,  length,  num_rotations,  expected_result): 
    print('Num Rotations = {}'.format(num_rotations) )

    print('Before Rotating: ', end='')
    LinkedList.display(head)

    head = LinkedList.rotate(head, num_rotations, length)
    LinkedList.compare(head, expected_result, length)

    print('After  Rotating: ', end='')
    LinkedList.display(head) 

    print('________________________________________')   



def test1(): 
    expected_result = [1]
    length = 1 
    num_rotations = 1

    #linked list initially contains 1->None 
    head = LinkedList.construct(length)
    perform_test(head, length, num_rotations, expected_result)



def test2():
    expected_result = [5, 1, 2, 3, 4]
    length = 5
    num_rotations = 1

    #linked list initially contains 1->2->3->4->5 
    head = LinkedList.construct(length)
    perform_test(head, length, num_rotations, expected_result)




def test3(): 
    expected_result = [4, 5, 1, 2, 3]
    length = 5 
    num_rotations = 2

    #linked list initially contains 1->2->3->4->5 
    head = LinkedList.construct(length)
    perform_test(head, length, num_rotations, expected_result)



def test4(): 
    expected_result = [2, 3, 4, 5, 1]
    length = 5
    num_rotations = 4

    #linked list initially contains 1->2->3->4->5 
    head = LinkedList.construct(length)
    perform_test(head, length, num_rotations, expected_result)



def test5():
    expected_result = [1, 2, 3, 4, 5]
    length = 5 
    num_rotations = 5

    #linked list initially contains 1->2->3->4->5 
    head = LinkedList.construct(length)
    perform_test(head, length, num_rotations, expected_result)


if (__name__ == '__main__'):
    test1()
    test2()
    test3()
    test4()
    test5()

    print('Test passed')
