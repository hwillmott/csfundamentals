class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def backtrack(count, curr, word, idx, results):
            if idx == len(word):
                if count > 0:
                    curr += str(count)
                results.append(curr)
                return
            backtrack(count+1, curr, word, idx+1, results)
            backtrack(0, curr + (str(count) if count > 0 else "") + word[idx], word, idx+1, results)
        
        results = []
        backtrack(0, "", word, 0, results)
        return results
        
        
        
                    
                    
                    
                    
                    