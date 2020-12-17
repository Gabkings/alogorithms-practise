class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " "* level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNone):
        self.children.append(TreeNode)



tree = TreeNode("Drinks",[])
cold = TreeNode("Cold", [])
hot = TreeNode("Warm", [])

tree.children.append(cold)
tree.children.append(hot)

coffee = TreeNode("Coffee", [])
tea = TreeNode("Tea", [])

hot.children.append(coffee)
hot.children.append(tea)
soda = TreeNode("Soda",[])
sprit = TreeNode("Spirit", [])
cold.children.append(soda)
cold.children.append(sprit)
print(tree)


