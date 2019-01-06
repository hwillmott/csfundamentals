import math
def swapBits(x, i, j):
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

def reverseBits(x):
    kWordSize = 2;
    kBitMask = 3;
    rev = [0, 2, 1, 3]
    return rev[x & kBitMask] << (3 * kWordSize) | rev[(x >> kWordSize) & kBitMask] << (2 * kWordSize) | rev[(x >> (kWordSize * 2)) & kBitMask] << kWordSize | rev[(x >> (kWordSize * 3)) & kBitMask]  

# returns the closest int to x with the same number of set bits
def closestInt(x):
    for i in range(8):
        if ((x >> i) & 1) != ((x >> (i + 1)) & 1):
            x ^= (1 << i) | (1 << (i+1))
            return x

def multiply(x, y):
    result = 0
    while(x):
        if(x & 1):
            result = add(result, y)
        x >>= 1
        y <<= 1
    return result

def add(a, b):
    result = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b
    while (temp_a or temp_b):
        ak = a & k
        bk = b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        result |= ak ^ bk ^ carryin
        carryin = carryout << 1
        k <<= 1
        temp_a >>= 1
        temp_b >>= 1
    return result | carryin

def divide(x, y):
    power = 32
    result = 0
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power = power - 1
        result += 1 << power
        x -= y_power
    return result

def power(x, y):
    result = 1.0
    power = y
    if y < 0:
        power = -power
        x = 1/x
    while power:
        if power & 1:
            result *= x
        x *= x
        power >>= 1
    return result

def reverseDecimal(x):
    isNegative = x < 0
    remaining = abs(x)
    result = 0
    while remaining:
        result = result * 10 + remaining % 10
        remaining /= 10
    return -result if isNegative else result

def isPalindrome(x):
    if x < 0:
        return "false"
    elif x == 0:
        return "true"
    num = math.floor(math.log10(x)) + 1
    mask = math.pow(10, num - 1)
    for i in range(int(num / 2)):
        if int(x / mask) != (x % 10):
            return "false: " + str(int(x / mask)) + " " + str(x % 10)
        x = x % mask
        x = int(x / 10)
        mask = mask / 100
    return "true"



print "swapBits(73, 1, 6) " + str(swapBits(73, 1, 6))
print "swapBits(37, 2, 3) " + str(swapBits(37, 2, 3))

print "reversing 10010011: " + str(bin(reverseBits(147)))

print bin(7)

print str(bin(closestInt(7)))

print multiply(5, 3)

print str(divide(15, 5))

print str(power(4, 3))

print str(reverseDecimal(12345))

print isPalindrome(1331)
print isPalindrome(123)
print isPalindrome(121)
