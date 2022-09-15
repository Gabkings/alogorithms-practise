from collections import defaultdict

def computePrice(map, price, discName):
    if(discName == None or discName == "EMPTY"):
        return price
    print(map, price, discName)

    d = map[discName]
    if d[0][0] == 0: return d[0][1]
    elif d[0][0] == 1: return round((1- (d[0][1] / 100)) * price)
    else: return price - d[0][1]

def findLowestPrice(products, discounts):
    map = defaultdict(list)

    for d in discounts:
        map[d[0]].append([int(d[1]), int(d[2])])
    total = 0

    for prod in products:
        price = int(prod[0])
        newPrice = price

        for i in range(1, len(prod)):
            newPrice = min(newPrice, computePrice(map, price, prod[i]))
        total += newPrice
    return total

products = [['10', 'd0', 'd1'],['15','EMPTY','EMPTY'],['20','d1','EMPTY']]

discounts = [['d0','1','27'],['d1','2','5']]

print(findLowestPrice(products, discounts))