def tandemBicycle(redShirtSpeed, blueShirtSpeed, fastest):
    redShirtSpeed.sort()
    blueShirtSpeed.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeed)

    totalSpeed = 0

    for idx in range(len(redShirtSpeed)):
        redier1 = redShirtSpeed[idx]
        rider2 = blueShirtSpeed[len(blueShirtSpeed) - idx - 1] # last element

        totalSpeed += max(redier1, rider2)

    return totalSpeed




def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

redShirtSpeed = [5,5,3,9,2]
blueShirtSpeed = [3,6,7,2,1]

fastest = False

print(tandemBicycle(redShirtSpeed, blueShirtSpeed, fastest))