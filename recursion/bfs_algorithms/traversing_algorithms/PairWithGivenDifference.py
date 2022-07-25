class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        size = len(A)

        # Initialize positions of two elements
        i, j = 0, 1

        # Search for a pair
        while i < size and j < size:

            if i != j and A[j]-A[i] == B:
                # print "Pair found (",A[i],",",A[j],")"
                return 1

            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1
        # print "No pair found"
        return 0
