class Solution:

    def reverseString(self, s):
        # remove extra space

        s = s.strip()

        # #to make sure we only get words split it to form list on space " ". The resultant list will have empty strings as element

        s = s.split(" ")

        # remove extra space we have this filter

        s = [i for i in s if i != ""]

        i = 0

        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1

        return " ".join(s)


sln = Solution()

s = "the sky is blue"

print(sln.reverseString(s))
