class Solution(object):
    def getletters(self, n):
        return {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
            '0': [' ']
            }[n]
    
    def backtrack(self, digits, indx, currstr, strs):
        if len(currstr) == len(digits):
            strs.append(currstr)
            return
        for letter in self.getletters(digits[indx]):
            self.backtrack(digits, indx+1, currstr+letter, strs)
            
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        strs = []
        self.backtrack(digits, 0, "", strs)
        return strs