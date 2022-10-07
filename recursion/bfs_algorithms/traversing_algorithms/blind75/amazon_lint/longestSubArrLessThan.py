import heapq

import collections

class Solution:

    def longestSubArr(self, nums, limit):
        maxHeap, minHeap = [],[]

        res = 1
        i = 0 
        for j in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[j], j))
            heapq.heappush(minHeap, (nums[j], j))

            if -maxHeap[0][0] - minHeap[0][0] > limit:
                i = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap and maxHeap[0][1] < i:
                    heapq.heappop(maxHeap)
                while minHeap and minHeap[0][1] < i:
                    heapq.heappop(minHeap)

            res = max(res, j-i+1)
        return res 

    def maxSumMinProduct(self, nums):
        n = len(nums)
        preSum = [0]*(n+1)
        left = [-1]*n 
        st = []
        for i in range(0, n):
            preSum[i+1] = preSum[i] + nums[i]
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st = []
        right = [n]*n 
        for i in range(n-1,-1,-1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)

        res = 0 
        for i in range(n):
            res = max(res, nums[i]*(preSum[right[i]] - preSum[left[i] + 1]))

        return res % (10**9 + 7)


    def subArraySum(self, nums, k):
        n = len(nums)
        preSum = [0]*(n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        res = 0 
        counts = collections.defaultdict(int)

        for i in range(n+1):
            if preSum[i] - k in counts:
                res += counts[preSum[i] - k]
            counts[preSum[i]] += 1 
        return res 

    def killProcess(self, pid, ppid, kill):
        graph = {}

        for i in range(len(pid)):
            if ppid[i] not in graph:
                graph[ppid[i]] = [pid[i]]

            else:
                graph[ppid[i]].append(pid[i])
        res = []

        q = collections.deque()

        q.append(kill)

        while q:
            pp = q.popleft()
            res.append(pp)
            if pp not in graph:
                continue
            for p in graph[pp]:
                q.append(p)

        return res 


sln = Solution()

nums = [8,2,4,7]
limit = 4 

nums1 = [2,3,3,1,2]

nums2 = [1,1,1]
k = 2



print(sln.longestSubArr(nums, limit))
print(sln.maxSumMinProduct(nums1))
print(sln.subArraySum(nums2, k))