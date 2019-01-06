class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        res += "-" if (numerator < 0) ^ (denominator < 0) else ""
        if numerator == 0 or denominator == 0: res = ""
        num, den = abs(numerator), abs(denominator)
        res += str(num/den)
        num %= den
        if num == 0: return res
        
        res += "."
        remainders = dict()
        remainders[num] = len(res)
        while num != 0:
            num *= 10
            res += str(num/den)
            num %= den
            if num in remainders:
                index = remainders[num]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                remainders[num] = len(res)
        return res