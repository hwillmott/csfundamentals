class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + " "
        l = len(s)
        end = 0
        for i in xrange(rows):
            end += cols
            while s[end % l] != ' ':
                end -= 1
            end += 1
        return end/l