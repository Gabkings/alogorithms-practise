def solution1(array, sequence):
    arrIdx = 0
    seqIdx = 0
    
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    
    return seqIdx == len(sequence)

def solution2(array, sequence):
    seqIdx = 0
    
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

print(solution1(array, sequence))
print(solution2(array, sequence))