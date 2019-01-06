def intersection(listA, listB):
    intersection = []
    countA = 0
    countB = 0
    while countA < len(listA) and countB < len(listB):
        if listA[countA] == listB[countB]:
            intersection.append(listA[countA])
            countA += 1
            countB += 1
        elif listA[countA] > listB[countB]:
            countB += 1
        elif listA[countA] < listB[countB]:
            countA += 1
    return intersection

def mergeSort(lst):
    if len(lst) > 1:
        middle = len(lst)//2
        leftList = lst[:middle]
        rightList = lst[middle:]

        leftList = mergeSort(leftList)
        rightList = mergeSort(rightList)
    
        mergedList = []

        l = 0
        r = 0
        while l < len(leftList) and r < len(rightList):
            if leftList[l] < rightList[r]:
                mergedList.append(leftList[l])
                l += 1
            else:
                mergedList.append(rightList[r])
                r += 1

        while l < len(leftList):
            mergedList.append(leftList[l])
            l += 1

        while r < len(rightList):
            mergedList.append(rightList[r])
            r += 1

        return mergedList
    return lst

def quickSort(lst, low, high):
    if low < high:
        pivot = partition(lst, low, high)
        
        quickSort(lst, low, pivot - 1)
        quickSort(lst, pivot + 1, high)

def partition(lst, low, high):
    pivot = lst[low]

    i = low + 1
    j = high
    done = False
    while not done:
        while i <= j and lst[i] <= pivot:
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i >= j:
            done = True
        else:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
    tmp = lst[low]
    lst[low] = lst[j]
    lst[j] = tmp
    return j

def mergeSortedListsInPlace(lstA, m, lstB, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if lstA[i] > lstB[j]:
            lstA[k] = lstA[i]
            i -= 1
            k -= 1
        else:
            lstA[k] = lstB[j]
            j -= 1
            k -= 1
    while i >= 0:
        lstA[k] = lstA[i]
        i -= 1
        k -= 1
    while j >= 0:
        lstA[k] = lstB[j]
        j -= 1
        k -= 1
    print lstA

def removeDupes(lst):
    lst = mergeSort(lst)
    result = []
    for i in range(0, len(lst)):
        if lst[i] != lst[i - 1]:
            result.append(lst[i])
    return result

print intersection([1,2,3,4,4,4,5,6,7,8,9,10,11,11,13,14], [1, 4, 7, 10, 12])
print mergeSort([1,5,8,2,4,0,8,6,1,2,2,3,8,6,4,7,5,9])
lst = [1,5,8,2,4,0,8,6,1,2,2,3,8,6,4,7,5,9]
quickSort(lst, 0, len(lst) - 1)
print lst
mergeSortedListsInPlace([5, 13, 17, -1, -1, -1, -1, -1], 3, [3, 7, 11, 19], 4)
print removeDupes([3, 17, 5, 12, 3, 4, 32, 4, 9, 11, 6, 3, 0, 18])
