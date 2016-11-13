class Graph:
    def __init__(self, vertices, connections, directed=False):
        self.graph = dict()
        self.directed = directed
        for v in vertices:
            self.graph[v] = set()
        self.addconnections(connections)

    def addconnections(self, connections):
        for v1, v2 in connections:
            self.addconnection(v1,v2)

    def addconnection(self, v1, v2):
        self.graph[v1].add(v2)
        if not self.directed:
            self.graph[v2].add(v1)
    
    def addvertex(self, v):
        if v not in self.graph:
            self.graph[v] = set()    
    
    def remove(self, v):
        del self.graph[v]
        for e in self.graph.values():
            if v in e:
                e.remove(v)

    def dfs(self, start, target):
        visited, path, stack = set(), [], [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                path.append(vertex)
                visited.add(vertex)
                if vertex == target:
                    return path
                stack.extend(self.graph[vertex] - visited)

        return path

    def bfs(self, start, target):
        visited, path, queue = set(), [], [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                path.append(vertex)
                visited.add(vertex)
                if vertex == target:
                    return path
                queue.extend(self.graph[vertex] - visited)
        return path


    def findpath(self, start, end):
        pass

    def print(self):
        print(self.graph)

def testbfsanddfs():
    g = Graph([1,2,3,4,5,6], [(1,2),(1,3),(3,4),(4,5),(4,6),(5,6)])
    g.print()
    print(g.dfs(1,4))
    print(g.dfs(1,8))
    print(g.bfs(1,4))
    print(g.bfs(1,8))
