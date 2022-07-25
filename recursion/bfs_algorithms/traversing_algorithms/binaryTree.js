//Node
class Node {
    constructor(key) {
        this.key = key
        this.left = null
        this.right = null
    }
}

//BST
class BST {
    constructor() {
        this.root = null;
    }

    insertNode = (node, newNode) => {
        if (newNode.key < node.key) {
            if (node.left === null) {
                node.left = newNode;
            } else {
                this.insertNode(node.left, newNode);
            }
        } else {
            if (node.right === null) {
                node.right = newNode;
            } else {
                this.insertNode(node.right, newNode);
            }
        }
    }

    //Insert
    insert = (key) => {
        let newNode = new Node(key);

        if (this.root == null) {
            this.root = newNode;
        } else {
            this.insertNode(this.root, newNode);
        }
    }

    //Search
    search = (key, node = this.root) => {
        if (node === null) {
            return false;
        }

        if (key < node.key) {
            return this.search(key, node.left);
        } else if (key > node.key) {
            return this.search(key, node.right);
        } else {
            return true;
        }
    }

    //Min
    min = (node = this.root) => {
        if (node) {
            while (node && node.left !== null) {
                node = node.left;
            }

            return node.key;
        }

        return null;
    }

    //Max
    max = (node = this.root) => {
        if (node) {
            while (node && node.right !== null) {
                node = node.right;
            }

            return node.key
        }

        return null;
    }


    bfs() {
        let node = this.root;
        let data = [];
        let queue = [];
        queue.push(node)
        while (queue.length) {
            node = queue.shift();
            data.push(node.key)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        return data
    }

    //Remove
    remove = (key) => {
        this.root = this.removeNode(this.root, key);
    }

    removeNode = (node, key) => {
        if (node === null) {
            return null;
        }

        if (key < node.key) {
            node.left = this.removeNode(node.left, key);
            return node;
        } else if (key > node.key) {
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
            node.key = aux.key;
            node.right = this.removeNode(node.right, aux.key);
            return node;
        }
    }

    maxDepth = () => {
        const calc = (node) => {
            if (!node) return 0
            return Math.max(1 + calc(node.left), 1 + calc(node.right))
        }
        return calc(this.root)
    };

    lowestCommonAncestor = (root, p, q) => {
        let lca = null
        const isCommonPath = (node) => {
            if (!node) return false
            var isLeft = isCommonPath(node.left)
            var isRight = isCommonPath(node.right)
            var isMid = node == p || node == q
            if (isMid && isLeft || isMid && isRight || isLeft && isRight) {
                lca = node
            }
            return isLeft || isRight || isMid
        }
        isCommonPath(root)
        return lca
    }


    isValidBST = () => {
        const helper = (node, min, max) => {
            if (!node) return true
            if (node.value <= min || node.value >= max) return false
            return helper(node.left, min, node.value) && helper(node.right, node.value, max)
        }
        return helper(this.root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER)
    }

    branchSums = () => {
        let sums = [];
        this.calculateBranchSums(this.root, 0, sums)
        return sums
    }

    calculateBranchSums = (node, runningSum, sums) => {
        if (!node) return
        let newRunningSum = runningSum + node.key;
        console.log(newRunningSum)
        if (!node.left && !node.right) {
            sums.push(newRunningSum)
        }

        this.calculateBranchSums(node.right, newRunningSum, sums)
        this.calculateBranchSums(node.left, newRunningSum, sums)

    }

    kthSmallest = (k) => {
        let val;

        let inorder = (this.root) {
            if (root == null) {
                return;
            }
            inorder(root.left);
            k--;

            if (k == 0) {
                val = root.key;
                console.log(val)
                return;
            }
            inorder(root.right);
        }
    }



}





const tree = new BST();
tree.insert(11);
tree.insert(7);
tree.insert(15);
tree.insert(5);
tree.insert(3);
// tree.insert(9);
// tree.insert(8);
// tree.insert(10);
// tree.insert(13);
// tree.insert(12);
// tree.insert(14);
// tree.insert(20);
// tree.insert(18);
// tree.insert(25);
// tree.insert(26);
// tree.insert(28);
// tree.insert(12);
// tree.insert(23);
// tree.insert(22);
// tree.insert(29);

// tree.remove(18);
// console.log(tree.min());
// console.log(tree.max());
// console.log(tree.search(18));
// console.log(tree.bfs())


// console.log(tree.maxDepth())
// console.log(tree.lowestCommonAncestor(3, 7))
// console.log(tree.branchSums())
console.log(tree.kthSmallest(2))