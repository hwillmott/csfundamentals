class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if rooms is None or len(rooms) == 0 or len(rooms[0]) == 0: return 
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue += (i,j),
                    
        for i,j in queue:
            for k,l in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
                if 0 <= k < len(rooms) and 0 <= l < len(rooms[0]) and rooms[k][l] == 2147483647:
                    rooms[k][l] = rooms[i][j] + 1
                    queue += (k,l),
        