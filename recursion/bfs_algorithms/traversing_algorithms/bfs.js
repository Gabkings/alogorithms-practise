class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearch {
    constructor() { this.root = null }

    insert(value) {
        let newNode = new Node(value)

        if (this.root === null) {
            this.root = newNode;
            return this;
        }

        let current = this.root;
        while (true) {
            if (value === current.value) return undefined;
            if (value < current.left) {
                if (current.left === null) {
                    current.left = newNode;
                    return this;
                }
                current = current.left

            } else {
                if (current.right === null) {
                    current.right = newNode
                    return this;
                }
                current = current.right
            }
        }
    }

    bfs() {
        let node = this.root;
        let data = [];
        let queue = [];
        queue.push(node)
        while (queue.length) {
            node = queue.shift();
            data.push(node.value)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        return data
    }

    search(value) {
        let node = this.root;
        let data = [];
        let queue = [];

        let found = false
        queue.push(node)
        while (queue.length) {
            node = queue.shift();
            if (node.value == value) {
                found = true
                break
            }
            data.push(node.value)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        return found
    }


    max = () => {
        let node = this.root
        if (node) {
            //Return the right most descendant's value
            while (node && node.right !== null) {
                node = node.right;
            }

            return node.value
        }

        return -1;
    }

    //Remove
    remove = (key) => {
        this.root = this.removeNode(this.root, key);
    }

    removeNode = (node, key) => {
        if (node === null) {
            return null;
        }

        if (key < node.value) {
            node.left = this.removeNode(node.left, key);
            return node;
        } else if (key > node.value) {
            node.right = this.removeNode(node.right, key);
            return node;
        } else {
            if (node.left === null && node.right === null) {
                node = null;
                return node;
            }
            if (node.left === null) {
                node = node.right;
                return node;
            } else if (node.right === null) {
                node = node.left;
                return node;
            }
            let aux = this.min(node.right);
            node.value = aux.value;
            node.right = this.removeNode(node.right, aux.value);
            return node;
        }
    }






}


const tree = new BinarySearch()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

// console.log(tree.bfs()) // [ 10, 6, 15, 3, 8, 20 ]

tree.remove(6)



console.log(tree.bfs()) // [ 10, 6, 15, 3, 8, 20 ]