class Solution:

    def splitString(self,s):
        n = len(s)

        def backtract(idx, parts, prev_val):
            if idx == n:
                return parts >= 2
            for i in range(idx, n):
                if prev_val == float("inf") or int(s[idx: i + 1]) == prev_val -1:
                    if backtract(i + 1, parts + 1, int(s[idx: i + 1])):
                        return True
            return False
        return backtract(0, 0, float("inf"))


s1 = Solution()

print(s1.splitString("1234"))