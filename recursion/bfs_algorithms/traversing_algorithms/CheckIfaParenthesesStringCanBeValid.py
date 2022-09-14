class Solution:

    def canBeValid(self, s, locked):
        if(len(s) % 2 != 0):
            return False

        #   lmin: min unmatched '('
        #   lmax: max unmatched '('
        
        lmax = 0
        lmin = 0

        for i in range(len(s)):
            if(locked[i] == "1"):
                if s[i] == "(":
                    lmin += 1
                    lmax += 1
                if s[i] == ")":
                    lmax -= 1
                    lmin -= 1
            else:
                lmax += 1
                lmin -= 1
            # invalid case
            if lmin < 0:
                lmin += 2
            if lmax < 0:
                return False
        return lmin == 0

    def checkValidString(self, s: str) -> bool:
        """ O(N)T O(1)S """
        a, b = 0, 0

        for c in s:
            if c == '(':
                a, b = a + 1, b + 1
            elif c == ')':
                a, b = a - 1, b - 1
            else:  # c=='*'
                a, b = a - 1, b + 1
            b < 0 and (b := math.inf)
            a < 0 and (a := 0)

        return a == 0 and b != math.inf

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        leftMax , leftMin = 0, 0

        for i in s:
            if i == "(":
                leftMax, leftMin = leftMax + 1, leftMin + 1
            elif i == ")":
                leftMax, leftMin = leftMax - 1, leftMin - 1
            else:
                leftMax, leftMin = leftMax + 1, leftMin - 1
            if leftMax < 0:
                return False
            if leftMin < 0: # s = (*)(
                leftMin = 0
        
        return leftMin == 0
        


sln = Solution()

s ="))()))"
locked ="010100"

print(sln.canBeValid(s, locked))