class Solution(object):
    def simplifyPath(self, path):
        startWithSlash = path[0]

        tokens = filter(self.filterHelper, path.split("/"))

        stack = []

        if startWithSlash == "/":
            stack.append("")

        for token in tokens:
            if token == "..":
                if len(stack) == 0 or stack[-1] == "..":
                    stack.append(token)
                elif stack[-1] != "":
                    stack.pop()
            else:
                stack.append(token)
        if len(stack) == 1 and stack[0] == "":
            return "/"
        return "/".join(stack)

    
    def filterHelper(self,token):
        return len(token) > 0 and token != ""

sl = Solution()

print(sl.simplifyPath("/../"))
print(sl.simplifyPath("//"))
print(sl.simplifyPath("/home/"))
print(sl.simplifyPath("/home//foo/"))
        