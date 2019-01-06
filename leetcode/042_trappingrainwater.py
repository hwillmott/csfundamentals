class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height)-1
        maxleft = 0
        maxright = 0
        result = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    result += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    result += maxright - height[right]
                right -= 1
        return result