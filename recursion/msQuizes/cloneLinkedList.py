class Node:
    def __init__(self, node):
        self.node = node
        self.next = None
        self.random = None


class LinkedList:
    def clone_list(self, root):

        '''Clone a doubly linked list with random pointer'''
        '''with O(1) extra space'''
        '''Insert additional node after every node of original list'''

        curr = root 

        while curr is not None:
            new_node = Node(1)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next 

        '''Adjust the random pointers of the newly added nodes'''
        while curr is not None:
            curr.next.random = curr.random.next 
            curr = curr.next.next 

        '''Detach original and duplicate list from each other'''
        dup_root = root.next 

        while curr.next is not None:
            tmp = curr.next 
            curr.next = curr.next.next 
            curr = temp 

        return dup_root 

    def print_dlist(root): 
        '''Function to print the doubly linked list'''
    
        curr = root 
        while curr != None: 
            print('Data =', curr.node, ', Random =', curr.random.node) 
            curr = curr.next