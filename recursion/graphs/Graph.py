class Graph:
    
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjancentVertx in self.gdict[deVertex]:
                if adjancentVertx not in visited:
                    visited.append(adjancentVertx)
                    queue.append(adjancentVertx)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjancentVertx in self.gdict[popVertex]:
                if adjancentVertx not in visited:
                    visited.append(adjancentVertx)
                    stack.append(adjancentVertx)



customGraph = {
    "a": ["b","c"],
    "b" : ["a","d","e"],
    "c": ["a", "e"],
    "d": ["b","e","f"],
    "e":["d","f","c"],
    "f": ["d", "e"]
}

graph = Graph(customGraph)
# print(graph.gdict)
print("BFS grapgh traversal")
graph.bfs("a")
print("DFS graph traversal")
graph.dfs("a")