# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create two pointers for easy traversal
        p1 = l1
        p2 = l2
        # Declare current carry over 
        currentCarry = 0 
        # Declare cur variable to help traverse the nodes and add them
        #Declare head to be the start node 
        head = cur = ListNode(0)
        
        # iterate over the the list 
        while p1 or p2 or currentCarry:
            currentVal = currentCarry
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            if currentVal >= 10:
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0
            cur.next = ListNode(currentVal)
            cur = cur.next 
            
            # Base cases for iterating linked list 
            if p1 is None and p2 is None:
                break 
            elif p1 is None:
                p2 = p2.next 
            elif p2 is None:
                p1 = p1.next 
            else:
                p1 = p1.next 
                p2 = p2.next 
        return head.next 




sample = Solution()

print(sample.addTwoNumbers(l1, l2))