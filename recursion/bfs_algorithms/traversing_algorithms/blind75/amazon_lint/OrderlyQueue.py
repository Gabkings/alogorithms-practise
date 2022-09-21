class Solution:

    def orderlyQueue(self, s, k):
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return "".join(sorted(s))


    def sum_subarray_min(self, a):
        MOD = 10**9 + 7

        stack = []

        ans = dot = 0 

        for i, y in enumerate(a):
            count = 1 
            while stack and stack[-1][0] >= y:
                x,c = stack.pop()
                count += c 
                dot -= x*c 
            stack.append((y, count))
            dot += y * count 
            ans += dot 
        return ans % MOD

sln = Solution()

s = "cba"
k = 1

a = [3,1,2,4]

print(sln.orderlyQueue(s, k))
print(sln.sum_subarray_min(a))