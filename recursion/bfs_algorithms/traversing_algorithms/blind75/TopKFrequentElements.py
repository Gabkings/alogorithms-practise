class Solution:

    def topKFrequent(self, nums, k):
        dicted = {}

        for i in range(len(nums)):
            if nums[i] not in dicted.keys():
                dicted[nums[i]] = 1
            else:
                dicted[nums[i]] += 1
        dicted = dict(sorted(dicted.items(), key=lambda x: x[1], reverse=True))

        result = list(dicted.keys())[:k]

        return result

# nums, k = [1,1,1,2,2,3], 2
nums, k = [4,1,-1,2,-1,2,3], 2


sln = Solution()

print(sln.topKFrequent(nums, k))