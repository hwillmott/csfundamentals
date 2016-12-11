class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        if len(s) == 0:
            results.append("")
            return results
        visited = set()
        queue = []
        
        visited.add(s)
        queue.append(s)
        found = False
        while len(queue) > 0:
            tmp = queue[0]
            queue = queue[1:]
            if self.isvalid(tmp):
                results.append(tmp)
                found = True
            if found: continue
            for i in range(len(tmp)):
                if tmp[i] != '(' and tmp[i] != ')': continue
                tmps = tmp[:i] + tmp[i+1:]
                if tmps not in visited:
                    queue.append(tmps)
                    visited.add(tmps)
        return results

    def isvalid(self,s):
        count = 0
        for l in s:
            if l == '(': count += 1
            elif l == ')': count -= 1
            if count < 0: return False
        return count == 0