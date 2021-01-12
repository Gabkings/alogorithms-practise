from collections import defaultdict

class Graph:
    def __init__(self, nodesVertes):
        self.gdict = defaultdict(list)
        self.nodesVertes = nodesVertes

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjancentVertx in self.gdict[vertex]:
                if adjancentVertx not in visited:
                    visited.append(adjancentVertx)
                    queue.append(adjancentVertx)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popStack = stack.pop(0)
            print(popStack)
            for adjancentVertx in self.gdict[vertex]:
                if adjancentVertx not in visited:
                    visited.append(adjancentVertx)
                    stack.append(adjancentVertx)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.gdict[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.gdict):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)

graph = Graph(8)

graph.addEdge("A", "C")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("F", "G")
graph.addEdge("B", "C")
graph.addEdge("B", "D")
graph.addEdge("D", "F")

graph.topologicalSort()