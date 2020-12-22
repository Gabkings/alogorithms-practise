def factorial(n):
    # unintensional case
    assert n >= 0 and n == int(n), "The number must ne interger and greater or equal to zero"
    # base case
    if n in [0,1]:
        return 1
    # recursive case
    return n * factorial(n-1)

print("factorial below")
print(factorial(4))

def fibonacii(n):
    # Unintensioanl case
    assert n > -1 and n == int(n), "N must be postive integer"
    # base case
    if n in [0,1]:
        return n
    # recursive case
    return fibonacii(n-1) + fibonacii(n-2)

print("fibonacii below")
print(fibonacii(4))

def sumOfDigits(n):
    # unintensional case
    assert n >= 0 and n == int(n), "n must be pisitive integer"
    # base case
    if n == 0:
        return 0
    # recursive case
    return int(n%10) + sumOfDigits(int(n/10))

print("sum below")
print(sumOfDigits(454)) 


def powerOfNumbers(base, expo):
    assert expo >= 0 and int(expo) == expo , "power must be greater than zero"
    if expo == 0:
        return 1
    elif expo == 1:
        return base
    return base * pow(base, expo - 1)

print("power below")

print(powerOfNumbers(2 , 4))

def gcd(num1, num2):
    assert num2 == int(num2) and num1 == int(num1) , "Numbers must be intergers"
    if num1 < 0:
        num1 = -1 * num1

    if num2 < 0:
        num2 = -1 * num2
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


print("gcd below")

print(gcd(48, 18))

def decimalToBinary(num):
    assert num == int(num) , f"{num} must be interger"

    if num == 0:
        return 0
    return num % 2 + 10 * decimalToBinary(int(num/2))

print("Decinamal to binary")
print(decimalToBinary(10))

from array import *

arr1 = array("i", [1,2,3,4,5,6,8,9,10])

# arr1.insert(0,8)

# print("Inserting element to a given index")
# print(arr1)

def accessElementByIndex(arr, index):
    if index >= len(arr):
        print(f"{index} does not exist")
    return arr[index]

print("Accessing element by index")
print(accessElementByIndex(arr1, 3))

def searchElementInArr(arr, element):
    for i in arr:
        if i == element:
            return arr.index(element)
    return f"{element} does not exist"

print("Searching element in array")
print(searchElementInArr(arr1, 3))

import numpy 

arr2 = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(arr2)

def traverse2DArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j])


print(traverse2DArr(arr2))

newArr2 = numpy.insert(arr2, 0, [[17,18,19,20]], axis=1)
print("Adding new column to 2D array")
print(newArr2)

newArr2 = numpy.insert(arr2, 0, [[17,18,19,20]], axis=0)
print("Adding new row to 2D array")
print(newArr2)

def access2DarrElement(arr, rowIndex, colIndex):
    if rowIndex >= len(arr) or colIndex >= len(arr[rowIndex]):
        return f" row index => {rowIndex} or column index ==> {colIndex} is out of range "
    return arr[rowIndex][colIndex]

print("Accessing element into 2D array")
print(access2DarrElement(newArr2, 3,2))

def traverse2Darr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            return arr[i][j]

print("Traversing 2D array")
print(traverse2DArr(newArr2))

def search2Darr(arr, element):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                return True
    return f"{element} does not exist"

print("Searching element in 2D array")
print(search2Darr(newArr2, 6))

def findMissingNum(myList, n):
    sum1 = n * (n+1)/2
    sum2 = sum(myList)
    return sum1 - sum2

print("Finding the missing number")
print(findMissingNum(arr1, 10))


def sumPairsTGivenNumber(myList, num):
    for i in range(len(myList)):
        for j in range(i+1, len(myList) ): 
            if (myList[i] + myList[j]) == num:
                print(myList[i], myList[j])
        

print("Pairs summation to given number ")
print(sumPairsTGivenNumber([2,6,3,9,4,4,11,5], 8))


def maxProductOfTwoInts(myList):
    maxProduct = 0
    for i in range(len(myList)):
        for j in range(i+1, len(myList) ): 
            if (myList[i] * myList[j]) >  maxProduct:
                maxProduct = myList[i] * myList[j]
                pair = str(myList[i]) +","+ str(myList[j])
    print(pair)
    print(maxProduct)
        

print("Max product of two numbers in array")
print(maxProductOfTwoInts([2,6,3,9,4,4,11,5]))

def isUnique(arr):
    a = []
    for i in arr:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print("Determine if all elements are unique")
print(isUnique(arr1))

def permutation(list1, list2):
    list2.reverse()
    if list1 == list2:
        return True
    return False

list1 = "keep".split()
list2 = "peek".split()

print("Determine if two works have same characters")
print(permutation(list1, list2))

def rotateMatrix(matrix):
    # find the number of rows
    n = len(matrix)
    # find the number of layers 
    for layer in range(n//2):
        first = layer
        last = n-layer-1  
        # Rotate the place of elements
        for i in range(first, last):
            # position of the top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move the bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move the right element to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move the top to the right
            matrix[i][-layer-1] = top

    return matrix


print("Matrix b4 rotation")
matrixArr = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrixArr)

print("Matrix rotation 90 Deg")

rotate1 = rotateMatrix(matrixArr)

print("Matrix rotation 180 Deg")
print(rotateMatrix(rotate1))

lst = ["SOLO", "hello", "Tea", "wHat"]

def count_uppercase(lst):
  count = 0
  
  # loop to access items in the list
  for i in range(len(lst)):
    word = lst[i]
    for j in range(len(word)):
        # print(word[j])
        if word[j].isupper():
            count += 1

  
  print(count)