class Solution:

    def twoSum(self, arr, k):
        arr.sort()

        left = len(arr) - 1
        right = 0

        while right < left:
            if right != left and arr[right] + arr[left] == k:
                return [right, left]
            elif arr[right] + arr[left] < k:
                right += 1
            else:
                left -= 1
        return -1


sln = Solution()
