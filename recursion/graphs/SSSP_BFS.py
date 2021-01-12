class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


    def bfs(self, start , end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjancentVertx in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjancentVertx)
                queue.append(new_path)


customGraph = {
    "A":["B","C"],
    "B":["D","G"],
    "C": ["C","D"],
    "D": ["F"],
    "E" : ["F"],
    "F" : ["G"],
    "G" : ["B","F"]
}

graph = Graph(customGraph)

s = graph.bfs("E","B")
print(s)