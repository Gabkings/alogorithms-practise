class Solution:

    def getMaxmumSumSubArrOfSizeK(self, inputArr, sizeK):

        if len(inputArr) == 0:
            return []

        maxSum = 0
        currentSum = 0
        startIndex = 0

        for index, element in enumerate(inputArr):
            currentSum += element

            if index < sizeK:
                maxSum = currentSum

            else:
                # we are over the max window size so remove 1 from left
                if(currentSum > maxSum):
                    maxSum = currentSum
                    startIndex = index - sizeK + 1

        return inputArr[startIndex:startIndex + sizeK]
        # return maxSum\


sln = Solution()

exampleInput1 = [-1, 2, 3, 0, -3, 9]
subarraySize1 = 2

print(sln.getMaxmumSumSubArrOfSizeK(exampleInput1, subarraySize1))
