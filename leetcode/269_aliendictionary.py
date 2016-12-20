class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        predecessors = dict()
        successors = dict()
        
        for w in words:
            for c in w:
                predecessors[c] = 0
        
        for w1,w2 in zip(words, words[1:]):
            for i in range(min(len(w1),len(w2))):
                if w1[i] != w2[i]:
                    succ = set()
                    if w1[i] in successors:
                        succ = successors[w1[i]]
                    if w2[i] not in succ:
                        succ.add(w2[i])
                        successors[w1[i]] = succ
                        predecessors[w2[i]] += 1
                    break
                        
        queue = {k: v for k, v in predecessors.items() if v == 0}.keys()
        order = ""
        while queue:
            val = queue.pop()
            order += str(val)
            if val in successors:
                for s in successors[val]:
                    predecessors[s] -= 1
                    if predecessors[s] == 0:
                        queue = [s] + queue
        if len(order) != len(predecessors): return ""
        return order