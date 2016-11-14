class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        length = len(height)
        head = 0
        tail = length - 1
        while tail > head:
            area = min(height[head], height[tail]) * (tail - head)
            maxArea = max(maxArea, area)
            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
                
        return maxArea