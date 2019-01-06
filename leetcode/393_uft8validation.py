class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def countStart(num):
            count = 0
            for i in range(8)[::-1]:
                    if not (b >> i) & 1: break
                    count += 1
            return count
        
        bytesLeft = 0
        
        for b in data:
            startBits = countStart(b)
            if bytesLeft == 0: 
                if startBits == 1 or startBits > 4:
                    return False
                if startBits == 0: 
                    bytesLeft = 0
                    continue
                bytesLeft = startBits - 1
                continue    
            if bytesLeft > 0: 
                if startBits != 1:
                    return False
                bytesLeft -= 1
        return True if bytesLeft <= 0 else False
            