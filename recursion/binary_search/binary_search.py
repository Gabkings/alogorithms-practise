def exact_match(arr, element):

    first, last = 0 , len(arr)-1

    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == element:
            return arr[mid]

        elif arr[mid] > element:
            last = mid - 1
        else:
            first = mid + 1

    return -1

arr = [1,2,3,5,8, 9, 10]\

element = 8;

# print(exact_match(arr, element))


def first_match(arr, element):

    lo, hi = 0, len(arr)-1

    res = -1 

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == element:
            res = mid 
            hi = mid -1
        elif arr[mid] > element:
            hi = mid - 1
        else:
            lo = mid + 1

    return res


def last_match(arr, element):
    lo , hi = 0 , len(arr)-1

    res = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == element:
            res = mid 
            hi = mid + 1

        elif arr[mid] > element:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return res


