def findAnagrams(stringList):
    d = dict()
    for string in stringList:
        sortedStr = sortString(string)
        if sortedStr in d:
            d[sortedStr].append(string)
        else:
            d[sortedStr] = [string]
    return d

def sortString(s):
    return ''.join(sorted(s))

def canStringBeAPalindrome(s):
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    numUnevenLetters = 0
    for key in d:
        if d[key] % 2 == 1:
            numUnevenLetters += 1
            if numUnevenLetters > 1:
                return False
    return True

def canAnonymize(letter, magazine):
    d = dict()
    for char in letter:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    for char in magazine:
        if char in d:
            d[char] -= 1
            if d[char] == 0:
                d.pop(char, None)
                if not d:
                    return True
    return False

strList = ["abba", "bbaa", "baba", "aabb", "cart", "ract", "bean"]
print findAnagrams(strList)
print canStringBeAPalindrome("edified")
print canStringBeAPalindrome("Bean")
print canAnonymize("abccdefgghijkk", "abbccccdeeeffahaklufgeuifhaegangqyugayukfelkljgsuehanwkfgaejyfbaegjb,ageyy")
print canAnonymize("bean", "bee")
