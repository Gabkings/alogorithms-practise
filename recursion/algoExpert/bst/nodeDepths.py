class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node":root, "depth": 0}]
    
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
        
    return sumOfDepths

def nodeDepthsV2(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepthsV2(root.left, depth +1) + nodeDepthsV2(root.right, depth + 1)

root = BinaryTree(10)

print(nodeDepths(root))
print(nodeDepthsV2(root))