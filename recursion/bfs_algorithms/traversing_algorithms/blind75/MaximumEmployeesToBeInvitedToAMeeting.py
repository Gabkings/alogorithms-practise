class Solution(object):
    def maximumInvitations(self, favorite):
        # 1st, check max single cycle
        fav = favorite
        n, seen, cycle = len(fav), set(), []
        for u in range(n):
            if u in seen:
                continue
            tseen = set()
            while u not in seen and u not in tseen:
                tseen.add(u)
                u = fav[u]
            else:
                if u in tseen:
                    cycle += u,
            seen |= tseen

        res = 0
        for s in cycle:
            c, ns = 1, fav[s]
            while ns != s:
                c, ns = c + 1, fav[ns]
            res = max(res, c) 
        
        # 2nd, check all cycle of 2 + their longest leaf
        G, couple = [[] for _ in range(n)], []
        for i, j in enumerate(fav):
            G[j] += i,
            if fav[j] == i and i < j:
                couple += [i, j],
                
        c = len(couple) * 2
        for i, j in couple:  # couples are guaranteed to be disconnected among each other because one can have only one fav
            stck = [(i, i, 0), (j, j, 0)]
            D = {i: 0, j: 0}
            while stck:
                cur, src, d = stck.pop()
                D[src] = max(D[src], d)
                for suc in G[cur]:
                    if suc != i and suc != j:
                        stck += (suc, src, d+1),
            c += sum(D.values())
        
        return max(c, res)

        