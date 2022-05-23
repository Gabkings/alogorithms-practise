
def nonConstructibleChange(coins):
    coins.sort()
    
    currentChange = 0
    
    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1
        currentChange += coin
        
    return currentChange + 1

print(nonConstructibleChange([1,2,5]))


def solution(A):
    A.sort()
    neg_count = len(list(filter(lambda x: (x < 0), A)))
    A = A[neg_count:]
    zeros_count = len(list(filter(lambda x: (x == 0), A)))
    if zeros_count > 0:
        return 0
    elif neg_count % 2 == 0:
        return 1
    else:
        return -1
