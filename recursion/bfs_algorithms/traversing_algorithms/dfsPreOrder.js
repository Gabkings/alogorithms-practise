class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
class BinarySearchTree {
    constructor() { this.root = null }

    insert(value) {
        if (this.root === null) {
            this.root = new Node(value)
            return this;
        }

        let current = this.root;
        let newNode = new Node(value)
        while (true) {
            if (value === current.value) return undefined;
            if (value < current.value) {
                if (current.left === null) {
                    current.left = newNode;
                    return this;
                }
                current = current.left
            } else {
                if (current.right === null) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            }
        }
    }

    DfsPreOder() {
        let data = [];

        function traverse(node) {
            data.push(node.value)
            if (node.left) traverse(node.left)
            if (node.right) traverse(node.right)
        }

        traverse(this.root)

        return data
    }
}

const tree = new BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

console.log(tree.DfsPreOder())