class Solution:
    """
    @param n: the length of the string.
    @param k: the kth Lexicographically smallest that result should be.
    @return: return the kth Lexicographically smallest string.
    """
    def kthString(self, n, k):
    # write your code here.
        sr=''
        total=3*pow(2,n-1)
        cal=0
        temp=0

        if k>total:
            return sr
        elif k<=total//3:
            sr+='a'
            cal=k-1
        elif k>total//3 and k<=(total*2)//3:
            sr+='b'
            cal=k-total//3-1
        else:
            sr+='c'
            cal=k-(total*2)//3-1

        for i in range(n-1,0,-1):
            temp=cal//pow(2,i-1)
            if temp==0:
                if sr[-1]=='a':
                    sr+='b'
                else:
                    sr+='a'
            else:
                if sr[-1]=='c':
                    sr+='b'
                else:
                    sr+='c'
            temp=cal//pow(2,i-1)
            cal=cal%pow(2,i-1)
            
        return sr