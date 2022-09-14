import math
import copy
from collections import defaultdict
from heapq import *

class Solution:
    def isRobotBounded(self, instructions):
        offset_dict_L = {}

        offset_dict_L[(0,1)] = (-1,0)
        offset_dict_L[(0,-1)] = (1,0)
        offset_dict_L[(1,0)] = (0,1)
        offset_dict_L[(-1, 0)] = (0,-1)

        offset_dict_R = {}
        offset_dict_R[(0,1)] = (1,0)
        offset_dict_R[(0,-1)] = (-1,0)
        offset_dict_R[(1,0)] = (0,-1)
        offset_dict_R[(-1,0)] = (0,1)

        cx = 0
        cy = 0

        c_offset = (0,1)

        for i in instructions:
            if(i == "G"):
                cx += c_offset[0]
                cy += c_offset[1]
            elif(i == "L"):
                c_offset = offset_dict_L.get(c_offset)
            elif(i == "R"):
                c_offset = offset_dict_R.get(c_offset)
        
        if(cx == 0 and cy == 0):
            return True
        elif(c_offset == (0,1)):
            return False
        else:
            return True 

    def stock_prices(self, stockPrice):
        #initialize month variable with 0
        month=0
        change=max(stockPrice)
        #Create a list to hold values
        l=[]
        total_sum = 0
        for i in range(len(stockPrice)):
            total_sum+=stockPrice[i]
        left = 0
        left_sum = 0
        while(len(stockPrice)>1):
            left = stockPrice.pop(0)
            l.append(left)
            #Now calculate the average
            left_sum += left
            avg1=left_sum //len(l)
            avg2=(total_sum-left_sum)//len(stockPrice)
            
            if(abs(avg1-avg2)<change): 
                change=abs(avg1-avg2) 
                month=len(l)

        return month

    def max_score(self, nums):
        def calc_score(nums, scores):
            if not nums:
                return 0
            if tuple(nums) in scores:
                return scores[tuple(nums)]
            n = len(nums) / 2
            max_score = 0
            for i in range(int(2*n)):
                for j in range(i+1, int(2*n)):
                    a = nums[i]
                    b = nums[j]
                    nums_copy = nums.copy()
                    # gcd = find_fcd(a,b)
                    nums_copy.remove(a)
                    nums_copy.remove(b)
                    score = int(n*math.gcd(a,b) + calc_score(nums_copy, scores))
                    if score > max_score:
                        max_score = score
            scores[tuple(nums)] = max_score
            return max_score

        return calc_score(nums, {})

    # shoping options / Find all combinations of numbers sum to target

    def print_all_sum_rec(self, target, current_sum, start, output, result):
        if current_sum == target:
            output.append(copy.copy(result))
        
        for i in range(start, target):
            temp_sum = current_sum + i
            if temp_sum <= target:
                result.append(i)
                self.print_all_sum_rec(target, temp_sum, i, output, result)
                result.pop()
            else:
                return
    
    def print_all(self, target):
        output = []
        result = []
        self.print_all_sum_rec(target, 0, 1, output, result)

        return output

    def maxmumUnits(self,B, T):
        B.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for b,n in B:
            boxes = min(b, T)
            ans += boxes * n
            T -= boxes
            if T == 0: return ans
        return ans

    def numPairDivisibleBy60(self, timeA):
        hashMap = defaultdict(int)
        count = 0
        for num in timeA:
            key = 60 - (num % 60)
            if key in hashMap:
                count += hashMap[key]
            elif key == 60:
                count += hashMap[0]
            hashMap[num % 60] += 1
        return count

    def slowestKey(self, releaseTimes, keysPressed):
        if keysPressed is None: return None
        if len(keysPressed) == 1: return keysPressed
        releaseTimes.insert(0,0)
        pressed_durations = []
        for i in range(1, len(releaseTimes)):
            duration_pressed = releaseTimes[i] - releaseTimes[i-1]
            pressed_durations.append((duration_pressed, i-1))
        longest_ord = 0
        longest_duration = float('-inf')
        answer = ""
        for duration, i in pressed_durations:
            char = keysPressed[i]
            if duration > longest_duration:
                longest_duration = max(longest_duration, duration)
                longest_ord = ord(char) - ord('a')
                answer = char
            elif duration == longest_duration:
                current_ord = ord(char) - ord('a')
                if current_ord > longest_ord:
                    longest_ord = max(longest_ord, current_ord)
                    answer = char
        return answer
    

    def maxAverageRatio(self, classes, extraStudent):
        computeGain = lambda p,t: (1 - (p/t)) / (t + 1)
        R = [(-computeGain(p,t), p,t) for p,t in classes]
        heapify(R)
        for x in range(extraStudent):
            _,p,t = heappop(R)
            p += 1
            t += 1
            heappush(R, (-computeGain(p,t),p,t))
        return sum(map(lambda x : x[1] / x[2], R)) / len(classes)

    # split string into unique primes
    def splitNum(self, s):
        assert "," not in s
        splits = []
        i = 0
        while i < 2**(len(s) - 1):
            b = str(bin(i))[2:]
            b = "0" * (len(s) - len(b)- 1) + b + "0"
            p = 0
            r = ""
            while p < len(s):
                r += s[p]
                if b[p] == "1":
                    r += ","
                p += 1

            nums = [int(x) for x in r.split(",")]
            splits.append(nums)
            i += 1
        return splits

    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if(n % 2 == 0):
                return False
        return True

    def arrAllPrime(self, s):
        for num in s:
            if not self.isPrime(num):
                return False
        return True

    def printSln(self, s):
        res = []
        for splits in self.splitNum(s):
            if self.arrAllPrime(splits):
                res.append(splits)
        return res

    # storage optimization 

    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        # sort both input list
        horizontalCuts.sort()
        verticalCuts.sort()

        # create a new list of Diff btw ALL horizontalCuts elements
        horDiffs = []
        for x in range(1, len(horizontalCuts)):
            horDiffs.append(horizontalCuts[x] - horizontalCuts[x-1])

        # Do the same for verticalCuts 
        verDiffs = []
        for x in range(1,len(verticalCuts)):
            verDiffs.append(verticalCuts[x] - verticalCuts[x-1])

        # Take the max values from both list of Diffs and multiply
        # take the modulo at the end
        return max(horDiffs) * max(verDiffs) % (10**9 + 7)

    def minDifficulty(self, D, K):
        if not D or not K or K > len(D): return -1
        N = len(D)
        maxInRange = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N): maxInRange[i][i] = D[i]
        for l in range(2, N+1):
            for i in range(N):
                j = i + l - 1
                if j >= N: continue
                maxInRange[i][j] = max(maxInRange[i+1][j-1], D[i], D[j])
        dp = [[float('inf') for _ in range(K+1)] for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(1, N + 1):
            for k in range(1, min(i,K) + 1):
                for j in range(k, i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + maxInRange[j-1][i-1])

        return dp[N][K]

    def minTrioDegree(self, n, edges):
        g = defaultdict(set)
        for a , b in edges:
            g[a].add(b)
            g[b].add(a)
        d = {n: len(g[n]) for n in g}
        inf = float("inf")
        res = inf
        for n in g:
            for m in g[n]:
                for o in g[n] & g[m]:
                    res = min(res, d[n] + d[m] + d[o] - 6)
                    g[0].discard(n)
                g[m].discard(n)
        return res if res < inf else -1

    def reorderLogFiles(self, logs):
        text, dig,res = [], [], []

        for i in logs:
            l = []
            items = i.split(" ")
            if items[1].isdigit():
                dig.append("".join(items))
            else:
                text.append((item[0], "".join(items[1:])))
        text.sort(key = lambda x:(x[1], x[0]))
        res = ["".join(tups) for tups in text]
        res.extend(dig)
        return res 




n, edges= 6, [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]  

jobDifficulty = [1,1,1]
d = 3

h, w, horizontalCuts, verticalCuts  = 5, 4, [1,2,4], [1,3]

s1 = "3175"

classes = [[1,2],[3,5],[2,2]]
extraStudent = 2

releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"


timeA = [30,20,150,100,40]
B = [[1,3],[2,2],[3,1]]
T = 4
nums = [3,4,6,8]
target = 4
stockPrice = [1,3,2,3]
instructions="GL"

sln = Solution()
print("Is Robot Bounded \n")
print(sln.isRobotBounded(instructions))
print("Stock prices \n")
print(sln.stock_prices(stockPrice))
print("Max Score \n")
print(sln.max_score(nums))
print("Shooping options \n")
print(sln.print_all(target))
print("Maxmising Units \n")
print(sln.maxmumUnits(B, T))
print("Num pair divisible by 60 \n")
print(sln.numPairDivisibleBy60(timeA))

print("Slowest keys \n")
print(sln.slowestKey(releaseTimes, keysPressed))

print("Max avarage ration \n")
print(sln.maxAverageRatio(classes, extraStudent))

print("Split string into unique primes \n")
print(sln.printSln(s1))

print("Storange optimization \n")
print(sln.maxArea(h, w, horizontalCuts, verticalCuts))

print("Job schedule \n")
print(sln.minDifficulty(jobDifficulty, d))

# print("Shooping patterns \n")
# print(sln.minTrioDegree(n, edges))

