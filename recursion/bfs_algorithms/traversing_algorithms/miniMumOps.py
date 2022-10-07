# Python3 implementation of the approach
import sys
import bisect
# Function to return the minimum operations
# required to make all array elements equal
def minOperations(arr, n) :

	# To store the frequency
	# of all the array elements
	mp = dict.fromkeys(arr, 0);

	# Traverse through array elements and
	# update frequencies
	for i in range(n) :
		mp[arr[i]] += 1;

	# To store the maximum frequency
	# of an element from the array
	maxFreq = -(sys.maxsize - 1);

	# Traverse through the map and find
	# the maximum frequency for any element
	for key in mp :
		maxFreq = max(maxFreq, mp[key]);

	# Return the minimum operations required
	return (n - maxFreq);

# Driver code
# if __name__ == "__main__" :

# 	arr = [2,2,1,3,1 ];
# 	n = 5 ;

# 	print(minOperations(arr, n));

# This code is contributed by Ryuga


class Solution:
    def kIncreasing(self, arr, k):
        def numReplaced(A):
            tail = []
            for a in A:
                if not tail or tail[-1] <= a:
                    tail.append(a)
                else:
                    tail[ bisect.bisect_right(tail, a)] = a
            return len(A) - len(tail)

        return sum(numReplaced(arr[i::k]) for i in range(k))

    def solve(self,num):
    
        first=""

        second=""

        length = len(num)

        num = sorted(num)

        for i in range(0,length,2):

            if length%2 and i==length-1:

                first += num[i]

            else:

                first += num[i]

                second += num[i+1]

        return int(first)+int(second)

    def getMinimunCost(self, parcels, k):
        n = len(parcels)

        res = []
        for i in range(1, k+1):
            if len(res) == (k - n):
                break
            if i not in parcels:
                res.append(i)

        return sum(res)

parcels = [6,5,4,1,3]
k = 7




sln = Solution()


arr = [4,1,5,2,6,2];
k = 3 ;

# print(sln.kIncreasing(arr, k))


def div_digit(n):
        
    lis=list(str(n))

    x,y='',''

    lis.sort()

    x=int(''.join(lis[::2]))

    y=int(''.join(lis[1::2]))

    return x+y

num = 1321

# print(sln.getMinimunCost(parcels, k))
# print(sln.kIncreasing(arr, n))
print(div_digit(num))