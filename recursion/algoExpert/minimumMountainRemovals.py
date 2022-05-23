def LIS(arr, flag):
    n = len(arr)
    deck = []
    dp = [1] * n
    for i in range(n):
        indx = bisect.bisect_left(deck, arr[i])
        if indx == len(deck):
            deck.append(0)
        dp[i] = indx
        deck[indx] = arr[i]

    return dp if flag == 1 else list(reversed(dp))


class Solution:
    def minimumMountainRemovals(self, nums):
        lis = LIS(nums, 1)
        lds = LIS(list(reversed(nums)), 0)
        n = len(nums)
        res = float('inf')
        for i in range(n):
            left = i - lis[i]
            right = (n - i - 1) - lds[i]
            if left == i or right == (n - i - 1):
                continue
            res = min(res, i - lis[i] + (n - i - 1) - lds[i])
        return res