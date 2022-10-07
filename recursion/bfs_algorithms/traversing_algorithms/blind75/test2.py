Given the root node of a binary tree, produce an algorithm that prints it level by level
and also reverses the order in which the nodes are printed for each level..
# 
# Example:
# 
#     1        <-
#    / \
#   2   3      ->1
#  / \   \
# 4  5    6    <-2
#   /      \
#  7        8  ->3
# 
# Result:
# 
# 1 2 3 6 5 4 7 8
# 
# Take a simple node:
# 
# Node {
#   Node left;
#   Node right;
#   int val;
# }


def levelOrderTraversal(root):
    res = []
    dfs(root, 0):
        
def dfs(node, level):
    
def bsf(node):
    myQue = [node]
    
    res = []
    res2 = []
    i = 1
    while myQue:
        n = myQue.pop(0)
        i += 1
        res.append(n.val)
        if n != None:
            if i % 2 == 0:
                res.extend(reverse(res2[n.val]))
            else:
                res.append(n.val)
            print(n.val)
            myQue.append(n.left)
            myQue.append(n.right)
        
# 1 2 3 4 5 6 7 8