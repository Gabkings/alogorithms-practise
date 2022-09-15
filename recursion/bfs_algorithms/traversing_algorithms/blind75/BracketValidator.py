class Solution:

    def __init__(self):
        self.open_list = ["[","{","("]
        self.close_list = ["]","}",")"]

    def check(self, myStr):
        stack = []

        for i in myStr:
            if i in self.open_list:
                stack.append(i)
            elif i in self.close_list:
                pos = self.close_list.index(i)
                if((len(stack) > 0) and (self.open_list[pos] == stack[len(stack) -1])):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 

sln = Solution()

myStr = "{[]{()}}"

print(sln.check(myStr))