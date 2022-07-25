class Solution:
    	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	# python code for above approach.

    def solve(self,A, B, C):

        # assigning the length -1 value
        # to each of three variables
        i = len(A) - 1
        j = len(B) - 1
        k = len(C) - 1

        # calculating min difference
        # from last index of lists
        min_diff = abs(max(A[i], B[j], C[k]) -
        min(A[i], B[j], C[k]))

        while i != -1 and j != -1 and k != -1:
            current_diff = abs(max(A[i], B[j],
            C[k]) - min(A[i], B[j], C[k]))

            # checking condition
            if current_diff < min_diff:
                min_diff = current_diff

            # calculating max term from list
            max_term = max(A[i], B[j], C[k])

            # Moving to smaller value in the
            # array with maximum out of three.
            if A[i] == max_term:
                i -= 1
            elif B[j] == max_term:
                j -= 1
            else:
                k -= 1
        return min_diff

# driver code



sln = Solution()


        
A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]

min_d = sln.solve(A, B, C)

print(min_d)