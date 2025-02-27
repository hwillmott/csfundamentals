class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strs = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        res = ""
        for i in range(len(strs)):
            while num >= vals[i]:
                num -= vals[i]
                res += strs[i]
        return res