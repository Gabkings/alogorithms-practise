class BinaryTree:
    # initializing binary tree
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        if self.lastUsedIndex == self.maxSize:
            return "Tree is full"
        else:
            self.customList[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            return "Inserted Succeessfully"
    def searchNode(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Success"
        return "Not found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            print(self.customList[index])
            self.preOrderTraversal(index*2)
            self.preOrderTraversal(index *2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)

    def postOderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.postOderTraversal(index * 2)
        self.postOderTraversal(index *2 +1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index , self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return " No node to delete"
        else:
            for i in range(1, self.lastUsedIndex):
                if self.customList[i] == value:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    return "Deleted successfully"
            return "Not found"

    def deletedBT(self):
        self.customList = None
        return "BT has been deleted"

newBt = BinaryTree(8)

print(newBt.insertNode("Drinks"))
print(newBt.insertNode("Hot"))
print(newBt.insertNode("Cold"))
print(newBt.insertNode("Tea"))
print(newBt.insertNode("Coffee"))
print(newBt.insertNode("Cola"))
print(newBt.insertNode("Spirit"))
print(newBt.searchNode(11))
print(newBt.deleteNode("Tea"))
print(newBt.levelOrderTraversal(1))
print(newBt.deletedBT())

    
      
    
    
	
