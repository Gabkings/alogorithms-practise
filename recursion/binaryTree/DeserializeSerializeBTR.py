class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left , self.right = None, None


class SerializeAndDeserialize:
    '''encode a tree into a string and decode it to binary tree'''
    
    def serialize(self, root):
        vals = []
        def preOrder(root):
            if not root:
                vals.append("#")
            else:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return " ".join(vals)

    def deserialize(self, data):
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popLeft()
                if val == '#':
                    return None 
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
            return root
        return build()

