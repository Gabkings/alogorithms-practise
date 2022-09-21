def find_first(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            if mid == 0 or a[mid - 1] != x:
                return mid 
            else:
                end = mid - 1
        elif a[mid] > x:
            end = mid - 1
        else:
            start = mid + 1 
    return -1  

def find_two_smallest(a):

    length = len(a)
    min_value = [1000, 1000]
    for cur_value in a:
        if cur_value < min_value[0]:
            min_value[1] = min_value[0]
            min_value[0] = cur_value
        elif cur_value < min_value[1]:
            min_value[1] = cur_value
    min_value.sort()

    return min_value[0], min_value[1]

def find_min_max(a):
    max_value = a[0]
    min_value = a[0]

    print(len(a))

    i = 0
    if len(a) % 2 == 1:
        max_value = min_value = a[0]
        i = 1
    while(i < len(a)):
        if(a[i] > a[i+1]):
            if( a[i] > max_value):
                max_value = a[i]
            if(a[i+1] < min_value):
                min_value = a[i+1]
        else:
            if(a[i] < min_value):
                min_value = a[i]
            if(a[i+1] > max_value):
                max_value = a[i+1]
        i += 2
    return min_value, max_value

print(find_two_smallest([2,7,3,4,5,5,5,6,3,6]))
print(find_min_max([2,7,3,4,5,5,1,5,9,6,3,6]))

        


print(find_first([1,2,3,4,5,5,5,6,3,6], 5))