def solution(a, d):
    card_months = 12
    my_dict = {}
    for i in range(len(a)):
        mon = d[i].split('-')[1]
        if my_dict.get(mon):
            if a[i] < 0:
                my_dict[mon][1].append(a[i])
            else:
                my_dict[mon][0].append(a[i])
        else:
            if a[i] < 0:
                my_dict[mon] = [[],[a[i]]]
            else:
                my_dict[mon] = [[a[i]], []]
    for entry in my_dict:
        if sum(my_dict[entry][1])* -1 >= 100:
            card_months -= 1
    total = sum(a) - card_months*5
    
    return total