
from collections import Counter
class Solution:

    def longestOnes(self, nums, k):
        start = end = 0
        zeros = 0
        res = 0
        while end < len(nums):
            zeros = zeros + abs(nums[end] - 1)
            while zeros > k:
                zeros = zeros - abs(nums[start] - 1)
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r-l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l = l + 1
            res = max(res, r-l+1)
            
        return res

    def lengthOfLongestSubstring(self, s):
        maxI = 0
        set1 = set()
        if len(s) == 0: return maxI 

        p1 = p2 = 0 

        while p2 < len(s):
            if(s[p2] in set1):
                set1.remove(s[p1])
                p1 += 1
            else:
                set1.add(s[p2])
                maxI = max(maxI , p2 - p1 + 1)
                p2 += 1

        return maxI


    def minWindow(self, s, t):
        S = len(s)
        T = len(t)
        t_dict = Counter(t)
        remaining_letters = T
        start = 0
        min_start = 0
        min_end = float('inf')
        
        for end in range(S):
            if not s[end] in t_dict:
                continue
            
            t_dict[s[end]] -= 1
            if t_dict[s[end]] >= 0:
                remaining_letters -= 1
            
            while not remaining_letters:
                if not s[start] in t_dict:
                    start += 1
                    continue
                
                window_size = end - start + 1
                min_substr_size = min_end - min_start + 1
                
                if window_size < min_substr_size:
                    min_start = start
                    min_end = end
                
                t_dict[s[start]] += 1
                if t_dict[s[start]] > 0:
                    remaining_letters += 1
                
                start += 1
        # print(s[min_start: min_end + 1] if min_end < float('inf') else '')
        
        return s[min_start: min_end + 1] if min_end < float('inf') else ''

    def minWindow2(self, s, t):
        ls, lt = len(s), len(t)
        s_counts, t_counts = Counter(), Counter(t)
        min_window, window = float('inf'), None
        st = en = shared = 0
        while en <= ls:
            
            if shared == lt: # try to shrink while we have all characters in t
                if en - st < min_window:
                    min_window, window = en - st, (st, en)
                s_counts[s[st]] -= 1
                if s_counts[s[st]] < t_counts[s[st]]:
                    shared -= 1 
                st += 1
            
            else: #try to expand if we need more characters to match t
                if en < ls:
                    s_counts[s[en]] += 1
                    if s_counts[s[en]] <= t_counts[s[en]]:
                        shared += 1
                en += 1
                
        return s[window[0]:window[1]] if window else ""



                







sln = Solution()

nums = [1,1,1,0,0,0,1,1,1,1,0]
k1 = 2

s = "ABAB"
k = 2

s1 = "abcabcbb"

s2 = "ADOBECODEBANC",
t = "ABC"

print(sln.characterReplacement(s, k))

print(sln.longestOnes(nums, k1))
print(sln.lengthOfLongestSubstring(s1))

print(sln.minWindow2(s2, t))