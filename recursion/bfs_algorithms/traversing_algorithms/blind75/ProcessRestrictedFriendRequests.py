class UnionFind2076:

    def __init__(self, size, restrictions):
        self.parent = [i for i in range(size)]
        self.restrictions = [0] * size
        self.all = [(1<<i) for i in range(size)]
        for a,b in restrictions:
            self.restrictions[a] |= (1<<b)
            self.restrictions[b] |= (1<<a)
    

    def find(self, n):
        m = n 
        while self.parent[m] != m:
            m = self.parent[m]
        while self.parent[n] != m:
            old_parent = self.parent[n]
            self.parent[n] = m 
            n = old_parent
        return m 

    def union(self, m, n):
        root_m, root_n = self.find(m), self.find(n)
        if root_m == root_n:
            return True 
        if self.restrictions[root_m]&self.all[root_n]:
            return False
        self.parent[root_m] = root_n 
        self.all[root_n] |= self.all[root_m]
        self.restrictions[root_n] |= self.restrictions[root_m]
        return True

class Solution:
    def friendRequest(self, n, restrictions, requests):
        uf = UnionFind2076(n, restrictions)
        res = [] 
        for a,b in requests:
            res.append(uf.union(a, b))
        return res 

sln = Solution()

n = 3
restrictions = [[0,1]]
requests = [[0,2],[2,1]]

print(sln.friendRequest(n, restrictions, requests))