from circularDLLPractical import LinkedList

def nth_element_to_last(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    return pointer1

cirList = LinkedList()

cirList.generateList(10, 0,99)

print(cirList)
print(nth_element_to_last(cirList, 4))