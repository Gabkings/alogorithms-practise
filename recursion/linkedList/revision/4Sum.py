class Solution(object):

    def fourSums(self, nums, target):
        nums = sorted(nums)
        res = []
        if not nums or len(nums) < 4:
            return res

        # if nums[0] + nums[1] + nums[2] + nums[3] > target:
        #     return res
        
        # if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
        #     return res
        
        for i in range(len(nums)):
            if nums[i] + nums[-1]+ nums[-2]+ nums[-3] < target:
                continue
            for j in range(i+1, len(nums)-2):
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                x = j + 1
                y = len(nums) - 1
                while x < y:
                    temp = nums[i] + nums[j] + nums[x] + nums[y]
                    if temp == target:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x = x + 1
                        while x < y and nums[x] == nums[x-1]:
                            x = x+1
                        x = x + 1
                    elif temp < target:
                        x = x + 1
                    else:
                        y = y -1

    
        # rr = []
        # for r in res:
        #     if r not in rr:
        #         rr.append(r)
        return res


sample = Solution()

print(sample.fourSums([1,0,-1,0,-2,2], 0))