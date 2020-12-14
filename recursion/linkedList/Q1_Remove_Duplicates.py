from circularDLLPractical import LinkedList

def remove_duplicates(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.next.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll


def remove_dups_without_buffer(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll


    

cirList = LinkedList()

cirList.generateList(10, 0,99)
print("Initial list")
print(cirList)
print("using buffer")
print(remove_duplicates(cirList))
print("without buffer")
print(remove_dups_without_buffer(cirList))
