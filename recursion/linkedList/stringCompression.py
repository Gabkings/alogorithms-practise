from itertools import *

# for i,j in groupby(map(int,list(input()))):
#     print(tuple([len(list(j)), i]),end="")
    
a = input()
z=[]
# group the same characters into a turple and applend it to list
b=[tuple(g) for k,g in groupby(a)]
print(b)
# loop throught the created list
for i in range(len(b)):
    # get the lenth of individual turple
    x=str(len(b[i]))
    # check length of the turple
    if len(b[i]):
        # pick the first element in the list
        y=str(b[i][0])
    else:
        # pick the element if len if is 1
        y=str(b[i])
    # push the computed values into the list
    z.append("("+x+", "+y+")")
print(" ".join(z))