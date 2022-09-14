import itertools
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas): return -1
        diff = list(itertools.accumulate([x - y for x, y in zip(gas, cost)]))
        return (diff.index(min(diff)) + 1) % len(diff)

    def canCompleteCircuit2(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res

sln = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(sln.canCompleteCircuit(gas, cost))
print(sln.canCompleteCircuit2(gas, cost))


