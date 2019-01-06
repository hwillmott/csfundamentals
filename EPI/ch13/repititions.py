import sys

def findNearestRepitition(text):
    d = dict()
    minDist = sys.maxint
    result = ""
    index = 0
    words = text.split()
    for string in words:
        if string in d:
            newMin = index - d[string][-1]
            if newMin < minDist:
                minDist = newMin
                result = string
            d[string].append(index)
        else:
            d[string] = [index]
        index += 1
    return result

def findShortestSubarray(text, words):
    d = dict()
    left = 0
    right = 0
    result = [-1, -1]
    paragraph = text.split()
    while right < len(paragraph):
        
        while right < len(paragraph) and len(d) < len(words):
            if paragraph[right] in words:
                if paragraph[right] in d:
                    d[paragraph[right]] += 1
                else:
                    d[paragraph[right]] = 1
            right += 1

        if len(d) == len(words):
            if (right - left) < (result[1] - result[0]) or result[0] == -1:
                result[0] = left
                result[1] = right

        while left < right and len(d) == len(words):
            if paragraph[left] in words:
                d[paragraph[left]] = d[paragraph[left]] - 1
                if d[paragraph[left]] == 0:
                    d.pop(paragraph[left], None)
                    if (result[1] - result[0]) > (right - left) or result[0] == -1:
                        result[0] = left
                        result[1] = right - 1
                    left += 1
                    break
            left += 1
    return result 


print findNearestRepitition("all work and no play makes no fun and no results")
print findShortestSubarray("apple banana apple apple dog cat apple dog banana apple cat dog", ["banana", "cat"])
print findShortestSubarray("apple banana apple apple dog cat apple dog banana apple cat dog", ["banana", "dog"])
