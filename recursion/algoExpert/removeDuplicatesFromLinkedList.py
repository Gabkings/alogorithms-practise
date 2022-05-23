class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList

    while currNode is not None:
        nextDinstinctNode = currNode.next

        while nextDinstinctNode is not None and nextDinstinctNode.value == currNode.value:
            nextDinstinctNode = nextDinstinctNode.next 

        currNode.next = nextDinstinctNode
        currNode = nextDinstinctNode

    return linkedList