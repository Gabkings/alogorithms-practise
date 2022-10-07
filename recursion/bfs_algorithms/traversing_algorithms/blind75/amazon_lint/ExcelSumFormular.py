
import collections
class Excel:

    def __init__(self, H, W):
        self.col = lambda c: ord(c) - ord("A")
        self.H, self.W = H, self.col(W) + 1
        self.values = collections.defaultdict(int)
        self.target = collections.defaultdict(lambda : collections.defaultdict(int))
        self.source = collections.defaultdict(lambda : collections.defaultdict(int))
        self.getIdx = lambda r,c: (r-1)*self.W + self.col(c)


    def updateTgt(self, idx, delta):
        queue = [idx]
        while queue:
            first = queue.pop(0)
            for tgt in self.target[first]:
                self.values[tgt] += self.target[first][tgt] * delta
                queue.append(tgt)

    def removeSrc(self, idx):
        for src in self.source[idx]:
            del self.target[src][idx]
        del self.source 

    def set(self, r, c, v):
        idx = self.getIdx(r,c)
        delta = v - self.values[idx]

        self.removeSrc(idx)
        self.updateTgt(idx, delta)

    def get(self,r, c):
        return self.values[self.getIdx(r,c)]

    def sum(self, r, c, strs):
        idx = self.getIdx(r,c)

        self.removeSrc(idx)
        cval = self.values[idx]
        self.values[idx] = 0 

        for src in strs:
            if ":" not in src:
                sc, sr = src[0], int(src[1:])
                sidx = self.getIdx(sr, sc)

                self.target[idx][sidx] += 1
                self.source[idx][sidx] += 1
                self.values[idx] += self.values[sidx]
            else:
                st,ed = src.split(":")
                for r in range(int(st[1:]), int(ed[1:]) + 1):
                    for c in range(self.col(st[0]), self.col(ed[0]) + 1):
                        sidx = (r-1)*self.W + c
                        self.target[sidx][idx] += 1
                        self.source[sidx][idx] += 1
                        self.values[idx] += self.values[idx]

        self.updateTgt(idx, self.values[idx] -cval)
        return self.values[idx]