class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


class Solution:

    def mergeTwoLists(self, l1, l2):
        # if both of the two lists are empty return the first empty list
        if not l1 and not l2:
            return l1
        # if only the first node is empty return the second and verse vasa
        if not l1:
            return l2
        if not l2:
            return l2

        # save the head which is equal to the begining and also get the tail of the merge linked list
        if(l1.val <= l2.val):
            head = l1
            newTail = l1 
            l1 = l1.next 
            newTail.next = l2 
        else:
            head = l2 
            newTail = l2 
            l2 = l2.next 
            newTail.next = l1 
        
        # while both linked lists have nodes left
        while(l1 and l2):
            # attach newTail to the smallest node and advance the respective pointer 
            if(l1.val <= l2.val):
                newTail.next = l1
                l1 = l1.next 
            else:
                newTail.next = l2 
                l2 = l2.next 
            newTail = newTail.next 
        if(l1):
            newTail.next = l1
        else:
            newTail.next = l2 
        return head



sln = Solution()

l1 = ListNode(1)
l1.next = 2
l1.next = 4

l2 = ListNode(1)
l2.next = 2 
l2.next = 3
l2.next = 4

print(l1.next.val)

# print(sln.mergeTwoLists(l1, l2))

     