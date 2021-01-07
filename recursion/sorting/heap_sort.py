from heapq import heappop, heappush 

def head_sort(nums):
    '''
    heappush(list, item): Adds an element to the heap, and re-sorts it afterward so that it remains a heap. Can be used on an empty list.
    heappop(list): Pops (removes) the first (smallest) element and returns that element. The heap remains a heap after this operation, so we don't have to call heapify().
    heapify(list): Turns the given list into a heap. It is worth noting that this method exists even though we won't be using this since we don't want to change our original array.
    '''
    # create an empty head 
    heap = []
    # insert the elements into heap and sort it
    for element in nums:
        heappush(heap, element)
    # create an empty list for display
    ordered = []
    while heap:
        # add items to ordered list
        ordered.append(heappop(heap))

    # return sorted list
    return ordered

s = [9,3,4,6,2,1,0,3,6,7,8]

print(head_sort(s))

