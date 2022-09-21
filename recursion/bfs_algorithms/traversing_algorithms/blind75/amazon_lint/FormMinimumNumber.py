import heapq
class Solution:

    def form_minimum_number(self, str):
        '''
        Given a pattern str containing only I and D. I for increasing and D for decreasing.
        Please design an algorithm to return the string that conforms to the pattern and
        has the smallest dictionary order. Digits from 1 to 9 and digits can’t repeat.
        '''
        lenght = len(str)

        answer = ""*lenght

        count = 1
        for i in range(lenght + 1):
            if i == lenght or str[i] == "I":
                for j in range(i-1, -2, -1):
                    answer = answer[:j+1] + chr(ord("0") + count) + answer[j+2:]
                    count += 1
                    if j >= 0 and str[j] == "I":
                        break 

        return answer 

    
    def validPermutationsDISequence(self, str):
        '''
        You are given a string s of length n where s[i] is either:

        'D' means decreasing, or
        'I' means increasing.
        A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:

        If s[i] == 'D', then perm[i] > perm[i + 1], and
        If s[i] == 'I', then perm[i] < perm[i + 1].
        Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.
        '''
        myStore = [1]
        for index, val in enumerate(str):
            if val == 0:
                continue
            temp = []

            for i in range(index + 2):
                if val == "I":
                    curr = sum(myStore[i:])
                else:
                    curr = sum(myStore[:i])
                temp.append(curr)
            myStore = temp
        return sum(myStore) % (10**9 + 7)

    def minimumCost2ConnectSticks(self, sticks):
        '''
        In order to decorate your new house, you need to process some sticks with positive integer length.
        You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.
        Due to the construction needs, you must connect all the bars into one.
        Return the minimum cost of connecting all the given sticks into one stick in this way.
        Please note that you can choose any order of sticks connection
        '''
        total_cost = 0 
        heap = sticks[:]

        heapq.heapify(heap)
        while len(heap) >= 2:
            cur_cost = heapq.heappop(heap) + heapq.heappop(heap)

            total_cost += cur_cost 
            heapq.heappush(heap, cur_cost)
        return total_cost

    def mergeStones(self, stones,k):
        # dp[i][j] represent total number of stones from i to j inclusive
        dp = [[float("inf") for i in range(len(stones))] for j in range(len(stones))]
        # if impossible to reduce stones into groups 
        if(len(stones) - 1) % (k-1) : return -1 

        prefix = [0]*(len(stones) + 1)
        for i in range(len(stones)):
            prefix[i+1] = prefix[i] + stones[i]
        
        def recursion(i, j):
            if dp[i][j] != float('inf'):
                return 
            if i + k> j + 1:
                # whereby we cannot reduce anymore
                dp[i][j] = 0 
                return
            for idx in range(i,j,k-1):
                # min(dp[i][j], left_half + right_half)
                recursion(i, idx)
                recursion(idx + 1, j)
                dp[i][j] = min(dp[i][j], dp[i][idx] + dp[idx + 1][j])

            if (j-i) % (k-1) == 0:
                # we can merge the groups
                dp[i][j] += prefix[j+1] - prefix[i]

        recursion(0, len(stones) - 1)
        return dp[0][len(stones) - 1]




sln = Solution()

str = "D"

sticks = [1,8,3,5]

# print(sln.form_minimum_number(str))
print(sln.minimumCost2ConnectSticks(sticks))
