
def search(arr, l, h):

    if l > h:
        return None
    
    if l == h:
        return arr[l]

    mid = l + (h - l)/2

    if mid % 2 == 0:

        if arr[mid] == arr[mid+1]:
            return search(arr, mid +2, h)
        return search(arr, l, mid)

    else:
        if arr[mid] == arr[mid -1]:
            return search(arr, mid+1, h)
        return search(arr, l, mid-1)

