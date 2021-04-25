def recursive_way(m,n):
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    return recursive_way(m-1, n) + recursive_way(m, n-1)



def memorization_way(m,n, memo={}):
    memo = {}
    keys = str(m)+","+str(n) 

    if keys in memo:
        return memo[keys]
    
    if m == 0 or n == 0:
        return 0 

    if m ==1 and n == 1:
        return 1
    
    memo[keys] = memorization_way(m-1, n, memo) + memorization_way(m,n-1, memo)

    return memo[keys]

c = memorization_way(30,30)
print(c)

