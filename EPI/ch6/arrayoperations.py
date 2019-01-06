import random
import sys

def createUnsortedArray(size, low, high):
    result = [random.randint(low, high) for x in range(size)]
    print(result)
    return result;

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    print("[", end='')
    for x in range(len(arr)):
        if (x == i) or (x == j):
            print("\033[91m" + str(arr[x]) + "\033[0m", end='')
        else:
            print(str(arr[x]), end='')
        if x != len(arr) -1:
            print(", ", end='')
    print("]")

def partitionByIndex(i, arr):
    pivot = arr[i]
    print(pivot)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < pivot:
                swap(arr, i, j)
                print("first pass, swapping " + str(i)  + " and " + str(j))
                print(arr)
                break

    for i in range(len(arr) - 1, -1, -1):
        if arr[i]  < pivot:
            break
        for j in range(i - 1, -1, -1):
            if arr[j] < pivot:
                break
            if arr[j] > pivot:
                swap(arr, i, j)
                print("second pass, swapping " + str(i) + " and " + str(j))
                print(arr)
                break

def partitionByIndexFaster(i, arr):
    pivot = arr[i]
    print(pivot)
    smIndex = 0;
    for i in range(len(arr)):
        if arr[i] < pivot:
            swap(arr, i, smIndex)
            print("first pass, swapping " + str(i) + " and " + str(smIndex))
            print(arr)
            smIndex += 1
    lgIndex = len(arr)-1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < pivot:
            break
        if arr[i] > pivot:
            swap(arr, i, lgIndex)
            print("second pass, swapping " + str(i) + " and " + str(lgIndex))
            print(arr)
            lgIndex -= 1

def threeIndices():
    arr = createUnsortedArray(10, 1, 3)
    firstValue = arr[0]
    print("firstValue = " + str(firstValue))
    pivotValue = -1
    lastValue = -1
    for i in range(len(arr)):
        if (arr[i] != firstValue) and (pivotValue == -1):
            pivotValue = arr[i]
            print("pivotValue = " +  str(pivotValue))
        elif (arr[i] != firstValue) and (arr[i] != pivotValue) and(lastValue == -1):
            lastValue = arr[i]
            print("lastValue = " + str(lastValue))
            break
    firstIndex = 0
    middleIndex = 0
    lastIndex = len(arr) -1
    for i in range(len(arr)):
        if arr[middleIndex] == firstValue:
            swap(arr, middleIndex, firstIndex)
            middleIndex += 1
            firstIndex += 1
        elif arr[middleIndex] == pivotValue:
            middleIndex += 1
        else:
            swap(arr, middleIndex, lastIndex)
            lastIndex -= 1
    print(arr) 

def fourIndices():
    arr = createUnsortedArray(15, 1, 4)
    values = []
    for i in range(len(arr)):
        if arr[i] not in values:
            values.append(arr[i])
    print(values)
    firstIndex = 0
    middleIndex = 0
    lastIndex = len(arr) - 1
    for i in range(len(arr)):
        if arr[middleIndex] == values[0]:
            swap(arr, middleIndex, firstIndex)
            middleIndex += 1
            firstIndex += 1
        elif arr[middleIndex] == values[1]:
            middleIndex += 1
        else:
            swap(arr, middleIndex, lastIndex)
            lastIndex -= 1
    middleIndex = lastIndex + 1
    lastIndex = len(arr) - 1
    for i in range(middleIndex, len(arr)):
        if middleIndex >= lastIndex:
            break
        if arr[middleIndex] == values[2]:
            middleIndex += 1
        else:
            swap(arr, middleIndex, lastIndex)
            middleIndex += 1
            lastIndex -= 1

def plusOne(arr):
    print(arr)
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 9:
            arr[i] += 1
            break
        else:
            arr[i] = 0
    if arr[0] == 0:
        arr[0] = 1
        arr.append(0)
    print(arr)

def reverse(arr):
    j = len(arr) - 1
    for i in range(len(arr)):
        if i >= j:
            break
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        j -= 1
    return arr

def multiply(arr1, arr2):
    arr1r = reverse(arr1)
    arr2r = reverse(arr2)
    result = [0 for x in range(len(arr1) + len(arr2))]
    for i in range(len(arr1r)):
        for j in range(len(arr2r)):
            result[i + j] += arr1r[i] * arr2r[j]
            result[i + j + 1] += int(result[i + j] / 10)
            result[i + j] %= 10
    resultr = reverse(result)
    for i in range(len(resultr)):
        if result[i] != 0:
            break
    print(resultr[i:])

def boardGameWalk(arr):
    farthest = 0
    for i in range(len(arr)):
        if i > farthest:
            break
        if farthest < i + arr[i]:
            farthest = i + arr[i]
    if farthest >= len(arr):
        print(len(arr) - 1)
    else:
        print(farthest)

def deleteKey(arr, key):
    printIndex = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[printIndex] = arr[i]
            printIndex += 1
    print(arr[:printIndex])

def deleteDuplicates(arr):
    lastValue = -1 
    printIndex = 0
    for i in range(len(arr)):
        if arr[i] != lastValue:
            arr[printIndex] = arr[i]
            printIndex += 1
            lastValue = arr[i]
    print(arr[:printIndex])

def buySellOnce(arr):
    maxProfit = 0
    topValue = 0
    minValue = arr[0]
    for i in range(len(arr)):
        sellTodayPrice = arr[i] - minValue
        if sellTodayPrice > maxProfit:
            maxProfit = sellTodayPrice
            topValue = arr[i]
        elif arr[i] < minValue:
            minValue = arr[i]
    print("buy at " + str(minValue) + " and sell at " + str(topValue) + " for a profit of " + str(maxProfit))

def generatePrimes(n):
    primes = [True for x in range(n)]
    primes[0] = False
    primes[1] = False
    i = 2
    while i * i < n:
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
        i += 1
    digits = []
    for i in range(n):
        if primes[i]:
            digits.append(i)
    print(digits)


#partitionByIndexFaster(3, createUnsortedArray(10,1,20))
#fourIndices()
plusOne([1,2,9])
plusOne([9,9,9])
#reverse([1,2,3,4,5])
#multiply([4,3],[2,1])
#multiply([1,2,3], [9,8,7])
#boardGameWalk([2, 4, 1, 1, 0, 2, 3])
#boardGameWalk([3, 2, 0, 0, 2, 0, 1])
#deleteKey([5, 3, 7, 11, 2, 3, 13, 5, 7], 3)
#deleteDuplicates([1,1,2,3,4,4,4,4,5,6,7,7,13])
#buySellOnce([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
#generatePrimes(200)
