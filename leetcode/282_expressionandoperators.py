class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        results = []
        self.backtrack(num, 0, "", target, 0, results, 0)
        return results
        
    def backtrack(self, num, index, path, target, curr, results, lastcur):
        if index == len(num):
            if curr == target:
                results.append(path)
            return
        for i in range(index,len(num)):
            if i != index and num[index] == '0': break
            tmp = int(num[index:i+1])
            if index == 0:
                self.backtrack(num, i+1, num[index:i+1], target, tmp, results, tmp)
            else:
                self.backtrack(num, i+1, path + "+" + num[index:i+1], target, curr + tmp, results, tmp)
                self.backtrack(num, i+1, path + "-" + num[index:i+1], target, curr - tmp, results, -tmp)
                self.backtrack(num, i+1, path + "*" + num[index:i+1], target, curr - lastcur + tmp*lastcur, results, tmp*lastcur)
                
                