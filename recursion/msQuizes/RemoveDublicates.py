
from collections import OrderedDict
class Solution:

    def removeDublicates(self, arr):
        return "".join(set(arr))

    def withoutOrder(self, arr):
        return "".join(OrderedDict.fromkeys(arr))
sample = Solution()

print(sample.removeDublicates("geekforgeeks"))

print(sample.withoutOrder("geekforgeeks"))