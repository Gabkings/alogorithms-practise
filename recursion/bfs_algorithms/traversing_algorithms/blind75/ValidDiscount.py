def findDiscountPattern(discount):
    mostLeft = 0
    left = 1
    while left < len(discount):
        if discount[mostLeft] == discount[left]:
            discount = discount[:mostLeft] + discount[left + 1:]
            mostLeft = 0
            left = 1
        else:
            mostLeft += 1
            left += 1
    if not len(discount):
        return True
    return False

def findCoupon(discounts):
    result = []
    for discount in discounts:
        if discount[0] == discount[-1]:
            discount = discount[1:-1]
            result.append(1 if findDiscountPattern(discount) else 0)
    return result

def checkValidity(_str):
    _str = list(_str)
    _ = {}
    test_list = []
    for i in _str:
        if i not in _:
            _[i] = "-"+i
    
    for i,j in enumerate(_str):
        if j in test_list:
            _str[i] = "-"+j
        else:
            test_list.append(j)
    test_list = []
    for i in _str:
        if i in _:
            test_list.append(i)
        elif i in _.values():
            if "-"+test_list[-1] == i:
                test_list.pop()
            else:
                return False
        else:
            return False 
    return True
    
_str = "xyffyxdd"
print(checkValidity(_str))

# O(n) time | O(1) space
def findMaximumSum(head):
	def reverseLinkedList(curr):
		prev, curr = None, curr
		while curr:
			temp = curr.next
			curr.next = prev
			prev, curr = curr, temp
		return prev

	slow = fast = head
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next

	slow.next = reverseLinkedList(slow.next)

	first, second = head, slow.next
	maxSum = 0
	while second:
		curSum = first.val + second.val
		maxSum = max(maxSum, curSum)
		first = first.next
		second = second.next
	return maxSum