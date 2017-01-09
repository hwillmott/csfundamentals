class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 is None or num2 is None or len(num1) == 0 or len(num2) == 0:
            return 0
        m = len(num1)
        n = len(num2)
        result = [0 for _ in range(m+n)]
        num1 = num1[::-1]
        num2 = num2[::-1]
        end = 0
        
        for i in range(m):
            for j in range(n):
                res = int(num1[i]) * int(num2[j])
                idx = i+j
                result[idx] += res
                while result[idx] > 9:
                  carry = result[idx]/10
                  result[idx] %= 10
                  idx += 1
                  result[idx] += carry
                if idx > end and result[idx] > 0:
                    end = idx
        resultstr = ""
        for i in range(end+1)[::-1]:
            resultstr += str(result[i])
        return resultstr
                      
                  
        