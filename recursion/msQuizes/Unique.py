myList = [12,34,55,67,7,4,6,4,7]

unique = []

for x in myList:
    itemExist = False
    for item in unique:
        if x == item:
            itemExist = True
            break
    if not itemExist:
        unique.append(x)

print(unique)