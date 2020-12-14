from circularDLLPractical import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail: 
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode
    # helper funtion to add same nodes 

def addSameNodes(lla, llb, value):
    tempNode = Node(value)
    lla.tail.next = tempNode
    lla.tail = tempNode
    llb.tail.next = tempNode
    llb.tail = tempNode

lla = LinkedList()
llb = LinkedList()

lla.generateList(7, 0,9)
print(lla)

llb.generateList(5, 0, 9)
print(llb)

addSameNodes(lla, llb, 8)
addSameNodes(lla, llb, 9)
addSameNodes(lla, llb, 3)

print(intersection(lla, llb))


    

