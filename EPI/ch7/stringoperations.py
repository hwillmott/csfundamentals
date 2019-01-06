import math

def stringToInt(s):
    idx = 1
    i = 0
    l = len(s)
    for x in s:
        i = i + int(x) * math.pow(10, (l - idx))
        idx += 1
    return int(i)

def intToString(i):
    s = ""
    while i:
        s = str(i % 10) + s
        i = int(i / 10)
    return s

def convertBase(s, b1, b2):
    i = 0
    for c in s:
        i = i * b1 + int(c)
    s2 = ""
    while i:
        tmp = i % b2
        s2 = getChr(tmp) + s2
        i = i / b2
    return s2

def getChr(i):
    return {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
            }.get(i, str(i))

def replaceAndRemove(s):
    writeIndex = 0
    strLen = 0
    for c in s:
        if c != 'b':
            s[writeIndex] = c
            writeIndex += 1
        if c == 'a':
            strLen += 1
    strLen += writeIndex
    writeIndex -= 1
    print(str(strLen) + " " + str(writeIndex))
    while writeIndex:
        if s[writeIndex] == a:
            s[strLen] = 'd'
            s[strLen - 1] = 'd'
            strLen -= 2
        else:
            s[strLen] = s[writeIndex]
            strLen -= 1
        writeIndex -= 1
    print(s)


print(intToString(23065113))
print(stringToInt("23065113"))


print(convertBase("615", 7, 13))

print(replaceAndRemove("acaa"))

