class Solution:
    def solve(self, matrix):
        def resolve(s):
            try:
                return int(s)
            except:
                return solve(*getIdx(s))

        def getIdx(s):
            return [int(s[1:]) - 1,ord(s[0]) - ord("A")]

        def do(a,b,op):
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b 

            if op == "/":
                return a / b

        def solve(i,j):
            try:
                return int(matrix[i][j])
            except:
                s = matrix[i][j]
                if s[0] == "=":
                    for c in s[2:]:
                        if c in "+-/*":
                            op = c 
                            break
                    a,b = s[1:].split(op)
                    aRes, bRes = resolve(a), resolve(b)
                    return do(aRes, bRes, op)

                else:
                    return solve(*getIdx(s))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = str(solve(i, j))

        return matrix 

sln = Solution()

matrix = [["B1", "7", "0"],["3", "5", "=A1+A2"]]

print(sln.solve(matrix))