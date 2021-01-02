class Solution:

    def fourSum(self,A,B,C, D):
        if len(A) == 0:
            return 0
        length = len(A)
        res = 0 
        dicts = {}
        for i in range(length):
            for j in range(length):
                twosum = A[i] + B[j]
                dicts[twosum] = dicts.get(twosum, 0) + 1
        
        for i in range(length):
            for j in range(length):
                res += dicts.get(-C[i] -D[j], 0)
        return res


sample = Solution()

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

print(sample.fourSum(A,B,C,D))