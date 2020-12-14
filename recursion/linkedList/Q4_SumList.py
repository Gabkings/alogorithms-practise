

from circularDLLPractical import LinkedList

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    return ll


circularList1 = LinkedList()
circularList2 = LinkedList()
print("List 1")
circularList1.generateList(3, 0,99)
print(circularList1)
print("List 2")
circularList2.generateList(3, 0,99)
print(circularList2)
print(sumList(circularList1, circularList2))