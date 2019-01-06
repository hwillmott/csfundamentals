def BinarySearch(lst, value):
    lower = 0
    upper = len(lst) - 1
    while lower < upper - 1:
        middle = int((upper-lower) / 2) + lower
        val = lst[middle]
        if val == value:
            return True
        if val > value:
            upper = middle - 1
        else:
            lower = middle + 1
    return False

def searchForFirstK(lst, k):
    lower = 0
    upper = len(lst) - 1
    result = -1
    while lower <= upper:
        middle = int((upper - lower) / 2) + lower
        val = lst[middle]
        if val == k:
            result = middle
            upper = middle - 1
        elif val > k:
            upper = middle - 1
        elif val < k:
            lower = middle + 1
    return result

def searchForFirstLargerThanK(lst, k):
    lower = 0
    upper = len(lst) - 1
    result = -1
    while lower <= upper:
        middle = int((upper - lower) / 2) + lower
        val = lst[middle]
        if val <= k:
            lower = middle + 1
        if val > k:
            result = middle
            upper = middle - 1
    return result

def searchSmallest(lst):
    lower = 0
    upper = len(lst) - 1
    result = -1
    while lower < upper - 1:
        middle = int((upper - lower) / 2) + lower
        val = lst[middle]
        if val < lst[lower]:
            upper = middle - 1
        elif val > lst[upper]:
            lower = middle + 1
    return lower

arr = [1,2,3,4,5,7,8,10,11,12,14]
print BinarySearch(arr, 11)
print BinarySearch(arr, 6)
arr2 = [1,2,3,4,5,6,7,7,7,8,9]
print searchForFirstK(arr2, 7)
arr3 = [1,1,2,3,4,5,6,7,8,9,9,10]
print searchForFirstK(arr3, 1)
print searchForFirstLargerThanK(arr3, 8)
print searchForFirstLargerThanK(arr3,9)

arr4 = [9, 10, 12, 1, 2, 3, 4, 5, 6, 7, 8]
print searchSmallest(arr4)

