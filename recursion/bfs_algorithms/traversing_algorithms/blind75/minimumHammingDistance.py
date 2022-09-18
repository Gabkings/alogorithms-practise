from collections import defaultdict, Counter, deque

class Solution:

    def minimumHammingDistance(self, source, target, allowedSwaps):

        ans = list(range(len(source)))

        def find(x):
            if x != ans[x]:
                ans[x] = find(ans[x])
            return ans[x]

        def union(x,y):
            px, py = find(x), find(y)

            if px != py:
                ans[py] = px 

        for i, j in allowedSwaps:
            union(i, j)

        dict1 , dict2 = defaultdict(list), defaultdict(list)
        for i in range(len(source)):
            dict1[find(i)].append(source[i])
            dict2[find(i)].append(target[i])
        total = 0

        for i in dict1.keys():
            total += sum((Counter(dict1[i])&Counter(dict2[i])).values())

        return len(source) - total

    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        graph = [set() for i in range(n)]
        for node1, node2 in pairs:
            graph[node1].add(node2)
            graph[node2].add(node1)
            result, visited = [0]*n, [False]*n 
            for i in range(n):
                if not visited[i]:
                    characters, indexes, dq = [],[], deque()
                    dq.append(i)
                    visited[i] = True
                    while dq:
                        node = dq.popleft()
                        indexes.append(node)
                        characters.append(s[node])
                        for nxt in graph[node]:
                            if not visited[nxt]:
                                dq.append(nxt)
                                visited[nxt] = True 
                    indexes.sort()

                    characters.sort()

                    for j, c in zip(indexes, characters):
                        result[j] = c 

        return "".join(result)

sln = Solution()

source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]

s = "dcab"
pairs = [[0,3],[1,2]]

print(sln.minimumHammingDistance(source, target, allowedSwaps))
print(sln.smallestStringWithSwaps(s, pairs))