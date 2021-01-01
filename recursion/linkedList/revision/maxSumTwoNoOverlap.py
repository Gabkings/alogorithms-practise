class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1,len(A)):
            A[i]+=A[i-1]
            
        res, Lmax, Mmax=A[L+M-1], A[L-1], A[M-1]
        for i in range(L+M,len(A)):
        # window  | --- L --- | --- M --- |
            Lmax=max(Lmax, A[i-M]-A[i-L-M])  
        # window  | --- M --- | --- L --- |
            Mmax=max(Mmax, A[i-L]-A[i-L-M])
            res= max(res,Lmax+A[i]-A[i-M], Mmax+A[i]-A[i-L])
            
        return res