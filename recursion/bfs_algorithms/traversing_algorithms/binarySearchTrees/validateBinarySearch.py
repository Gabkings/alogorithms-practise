class Solution:

    def isValidBST(self, root):
        def validate(root, minValue, maxValue):
            if root is None:
                return True
            if root.val <= minValue or root.val >= maxValue:
                return False
            return validate(root.left, minValue, root.val) and validate(root.right, root.val, maxValue)
        return validate(root, -2**32-1, 2**32)