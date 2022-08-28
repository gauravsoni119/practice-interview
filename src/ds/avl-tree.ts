/**
 * Binary Tree
 *
 * @example
 * const linkedList = require('binary-tree');
 *
 * @author Gaurav Soni
 *
 * @module ds/binary-tree
 *
 */

/**
 * A node inside a AV: tree.
 *
 * @public
 * @constructor
 *
 * @param {unknown} val - The value stored in the AV: tree
 */
export class TreeNode<T> {
	/**
	 * Value of the tree node.
	 * @member {Object}
	 */
	public value!: T;
	/**
	 * Left node
	 * @member {TreeNode}
	 */
	left: TreeNode<T> | null = null;
	/**
	 * Right node
	 * @member {TreeNode}
	 */
	right: TreeNode<T> | null = null;
	/**
	 * Height of the node
	 * @member {number}
	 */
	height = 0;

	constructor(
		value: T,
		left: TreeNode<T> | null,
		right: TreeNode<T> | null,
		height: number
	) {
		this.value = value;
		this.left = left;
		this.right = right;
		this.height = height;
	}
}

/**
 * AVL Tree
 *
 *
 * @public
 * @constructor
 */
export class AVLTree<T> {
	root: TreeNode<T> | null = null;

	/**
	 * Insert the node into the AVL tree at given node. If not provided, root will be consider as current. <br><br>
	 * Time Complexity: O(logN) in the average case and O(N) in worst case.
	 *
	 * @public
	 * @method
	 * @param value value that needs to be inserted
	 * @param current Current Node
	 * @returns void
	 */
	insert(value: T, current: TreeNode<T> | null = null): void {
		if (!this.root) {
			this.root = new TreeNode(value, null, null, 1);
			return;
		}
		current = current || this.root;
		let insertKey: keyof TreeNode<T>;
		if (current.value > value) {
			insertKey = 'left';
		} else {
			insertKey = 'right';
		}
		if (current && !current[insertKey]) {
			current[insertKey] = new TreeNode(value, null, null, 0);
		} else {
			this.insert(value, current[insertKey]);
		}
	}

	/**
	 * Given the root of a binary tree, invert the tree, and return its root.
	 * <br />
	 * For example,
	 * <br />
	 * <b>Input:</b> [4, 2, 7, 1, 3, 6, 9]
	 * <br />
	 * <b>Output:</b> [4, 7, 2, 9, 6, 3, 1]
	 * <br />
	 *
	 * @method
	 * @see {@link https://leetcode.com/problems/invert-binary-tree/|Invert Binary Tree}
	 *
	 * @public
	 *
	 * @returns {TreeNode} Inverted AVL tree
	 */

	invert(): TreeNode<T> | null {
		function invert(root: TreeNode<T> | null) {
			if (!root) {
				return null;
			}
			const left = root.left;
			root.left = invert(root.right);
			root.right = invert(left);
			return root;
		}
		return invert(this.root);
	}

	/**
	 * Given the root of a binary tree, return its maximum depth/height.
	 * <br /><br />
	 * A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
	 * For example,
	 * <br />
	 * <b>Input:</b> [3, 9, 20, null, null, 15, 7]
	 * <br />
	 * <b>Output:</b> 3
	 * <br />
	 *
	 * @method
	 * @see {@link https://leetcode.com/problems/maximum-depth-of-binary-tree/|Maximum Depth of Binary Tree}
	 *
	 * @public
	 *
	 * @returns {Number} Diameter of AVL tree
	 */

	getHeight(): number {
		function maxDepth(root: TreeNode<T> | null): number {
			if (!root) {
				return 0;
			}
			return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
		}
		return maxDepth(this.root);
	}

	/**
	 * Given the root of a binary tree, return the length of the diameter of the tree
	 * <br /><br />
	 * The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
	 * For example,
	 * <br />
	 * <b>Input:</b> [1, 2, 3, 4, 5]
	 * <br />
	 * <b>Output:</b> 3
	 * <br />
	 *
	 * @method
	 * @see {@link https://leetcode.com/problems/diameter-of-binary-tree/|Diameter of Binary Tree}
	 *
	 * @public
	 *
	 * @returns {Number} Height of AVL tree
	 */

	getDiameter(): number {
		let ans = 0;
		function diameterOfBinaryTree(root: TreeNode<T> | null): number {
			if (!root) {
				return 0;
			}
			const left = diameterOfBinaryTree(root.left);
			const right = diameterOfBinaryTree(root.right);
			ans = Math.max(left + right, ans);
			return 1 + Math.max(left, right);
		}
		diameterOfBinaryTree(this.root);
		return ans;
	}

	/**
	 * Given a binary tree, determine if it is height-balanced.
	 * <br /><br />
	 * a height-balanced binary tree is defined as:
	 * "a binary tree in which the left and right subtrees of every node differ in height by no more than 1."
	 * For example,
	 * <br />
	 * <b>Input:</b> [3, 9, 20, null, null, 15, 7]
	 * <br />
	 * <b>Output:</b> true
	 * <br />
	 *
	 * @method
	 * @see {@link https://leetcode.com/problems/balanced-binary-tree/|Balanced Binary Tree}
	 *
	 * @public
	 *
	 * @returns {boolean} Tree is balanced or not
	 */

	isBalanced(): boolean {
		function checkBalanced(root: TreeNode<T> | null): number {
			if (!root) {
				return 0;
			}
			const left = checkBalanced(root.left);
			if (left === -1) return -1;
			const right = checkBalanced(root.right);
			if (right === -1) return -1;
			return Math.abs(left - right) > 1 ? -1 : 1 + Math.max(left, right);
		}
		return checkBalanced(this.root) > -1 ? true : false;
	}

	/**
	 * Given the roots of two binary trees p and q, write a function to check if they are the same or not.
	 * <br /><br />
	 * Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
	 * For example,
	 * <br />
	 * <b>Input:</b> p = [1, 2, 3], q = [1, 2, 3]
	 * <br />
	 * <b>Output:</b> true
	 * <br />
	 *
	 * @static
	 * @function
	 * @see {@link https://leetcode.com/problems/same-tree/|Same Tree}
	 *
	 * @public
	 *
	 * @returns {boolean} Both trees are same or not
	 */

	static isSameTree<T>(tree1: AVLTree<T>, tree2: AVLTree<T>): boolean {
		function sameTree(
			root1: TreeNode<T> | null,
			root2: TreeNode<T> | null
		): boolean {
			if (!root1 && !root2) return true;
			if (!root1 || !root2 || root1.value !== root2.value) return false;
			const isLTreeSame = sameTree(root1.left, root2.left);
			const isRTreeSame = sameTree(root1.right, root2.right);
			return isLTreeSame && isRTreeSame;
		}
		return sameTree(tree1.root, tree2.root);
	}
}
