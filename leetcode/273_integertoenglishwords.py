class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        #deal with edge cases (0)
        if num == 0: return "Zero"
        
        s = ""
        if num >= 1000000000:
            s += self.wordsFromNumber(num / 1000000000)
            s += " Billion"
            num %= 1000000000
        if num >= 1000000:
            if len(s) > 0: s += " "
            s += self.wordsFromNumber(num / 1000000)
            s += " Million"
            num %= 1000000
        if num >= 1000:
            if len(s) > 0: s += " "
            s += self.wordsFromNumber(num / 1000)
            s += " Thousand"
            num %= 1000
        if num > 0:
            if len(s) > 0: s += " "
            s += self.wordsFromNumber(num)
            
        return s
        
        
    def wordsFromNumber(self,num):
        s = ""
        d = { 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
        teens = { 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        tens = { 2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
        if num >= 100:
            s += str(d[num/100]) + " Hundred"
        num = num % 100
        if num >= 20:
            if len(s) > 0: s += " "
            s += str(tens[num/10])
            num = num % 10
        if num >= 10:
            if len(s) > 0: s += " "
            s += str(teens[num])
            num = 0
        if num > 0:
            if len(s) > 0: s += " "
            s += str(d[num])
        return s
            
            
            
            
            
            
            
            