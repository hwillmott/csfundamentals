class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def backtrack(hours, minutes, hoursi, minutesi, bits, num, results):
            if bits == num:
                #check if valid time
                if hours < 12 and minutes <= 59:
                    s = "{}:{:02d}".format(hours, minutes)
                    results.add(s)
                return
            for i in range(hoursi, 4):
                if not (hours >> i) & 1:
                    backtrack(hours | (1 << i), minutes, i, minutesi, bits+1, num, results)
            for i in range(minutesi, 6):
                if not (minutes >> i) & 1:
                    backtrack(hours, minutes | (1 << i), hoursi, i, bits+1, num, results)
        results = set()
        backtrack(0,0,0,0,0,num,results)
        return sorted(results)