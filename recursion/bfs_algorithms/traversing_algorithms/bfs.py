class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


    def bfs(self, root):
        if root is None:
            return 

        queue = [root]

        while len(queue) > 0:
            cur_node = queue.pop(0)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)

            print(queue)

    def maxLevelSum(self, root):        
        sum, l, ans = float('-inf') , 1, 0       
        if root is not None:
            queue = [root]
            while len(queue) > 0:   
                s = 0
                for _ in range(len(queue)):
                    cur_node = queue.pop(0) 
                    s += cur_node.val  
                    if cur_node.left is not None:
                        queue.append(cur_node.left)
                    if cur_node.right is not None:
                        queue.append(cur_node.right)
                if s > sum:
                    sum = s
                    ans = l                 
                l += 1
        return ans

    def averageOfLevels(self, root):
        res = []
        if root is not None:
            queue = []
            queue.append(root)
            while len(queue):   
                s = 0
                n = len(queue)
                for _ in range(n):
                    cur_node = queue.pop(0) 
                    s += cur_node.val  
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
                print(s, n)
                res.append(s/n)                
        return res

    def levelOrderBottom(self, root):
        
        if root is None:
            return []
        queue = [root]
        
        res = []
        
        while queue:
            resLv = []
            
            n = len(queue)
            
            for _ in range(n):
                cur_node = queue.pop(0)
                resLv.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                    
            res.append(resLv)
            
        return res[::-1]

    def zigzagLevelOrder(self, root):        
        if root is None:
            return []
        queue = [root]
        
        res = []
        
        l = 0
        
        while queue:
            resLv = []
            
            n = len(queue)
            
            for _ in range(n):
                cur_node = queue.pop(0)
                  
                
                if l % 2 == 0:
                    
                    resLv.append(cur_node.val)

                    if cur_node.right:
                        queue.append(cur_node.right)
                    if cur_node.left:
                        queue.append(cur_node.left)
                else:
                    resLv.append(cur_node.val)

                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
            l += 1
            print(l)
                    
            res.append(resLv)
            
            
        return res

    def zigzagLevelOrder2(self, root):
        if not root: return []
        queue = [root]
        result, direction = [], 1
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result

    def deepestLeavesSum(self, root):
        q, ans, qlen, curr = [root], 0, 0, 0
        while len(q):
            qlen, ans = len(q), 0
            for _ in range(qlen):
                curr = q.pop(0)
                ans += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        return ans
        
                
            


    def insert_node(self, value):
        if value is not None:
            if value < self.val:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert_node(value)

            if value > self.val:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert_node(value)

    @staticmethod
    def insert_nodes(vals, root):
        for i in vals:
            root.insert_node(i)

# sln = root = Node(4)
# vals = [2, 1, 3, 6, 5, 7]
# sln.insert_nodes(vals, root)

# sln.bfs()

def run():
    root = Node(4)
    root.insert_nodes([2, 1, 3, 6, 5, 7], root)
    root.bfs(root)

run()
    
