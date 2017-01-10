class WeightedGraph:
    def __init__(self, vertices=[], connections=[]):
        self.graph = dict()
        for v in vertices:
            self.graph[v] = dict()
        self.addconnections(connections)

    def addconnections(self, connections):
        for c in connections:
            self.addconnection(c)
    
    def addconnection(self, connection):
        v1, v2, weight = connection
        self.graph[v1][v2] = weight
        self.graph[v2][v1] = weight

    # shortest path, O(V^2) where V is number of vertices
    def dijkstra(self, source):
        unvisited = {node: None for node in self.graph.keys()}
        visited = {}
        curr = source
        currdist = 0
        unvisited[source] = currdist

        while True:
            for neighbor, distance in self.graph[curr].items():
                if neighbor not in unvisited:
                    continue
                newdist = currdist + distance
                if unvisited[neighbor] is None or unvisited[neighbor] > newdist:
                    unvisited[neighbor] = newdist
            visited[curr] = currdist
            del unvisited[curr]
            if not unvisited:
                break
            candidates = [node for node in unvisited.items() if node[1]]
            curr, currdist = sorted(candidates, key=lambda x: x[1])[0]
        print(visited)

    # minimum spanning tree
    def prim(self, start):
        mst = WeightedGraph(vertices=self.graph.keys())
        visited = set()
        numV = len(self.graph.keys())
        visited.add(start)
        
        while len(visited) < numV:
            crossing = set()
            for v in visited:
                for k in self.graph.keys():
                    if k not in visited and k in self.graph[v]:
                        crossing.add((v,k,self.graph[v][k]))

            edge = sorted(crossing, key=lambda e: e[2])[0]
            mst.addconnection(edge)
            visited.add(edge[1])
        print(mst)

    def __str__(self):
        return str(self.graph)

def testWeightedGraph():
    g = WeightedGraph(['A','B','C','D','E','F'],[('A','B',7),('A','C',9),('A','F',14),('B','C',10),('B','D',15),('C','D',11),('C','F',2),('D','E',6),('E','F',9)])
    #print(g)
    #g.dijkstra('A')
    g.prim('A')


testWeightedGraph()
