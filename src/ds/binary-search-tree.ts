/**
 * Binary Search Tree
 *
 * @example
 * import { BinarySearchTree } from '../../ds/binary-search-tree';
 * const bst = new BinarySearchTree();
 * bst.insert(10);
 * bst.insert(5);
 * bst.insert(8);
 * bst.insert(4);
 * bst.insert(6);
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
export class BinarySearchTree<T> {
	root: TreeNode<T> | null = null;

	/**
	 * Insert the node into the binary tree at given node. If not provided, root will be consider as current. <br><br>
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
	 * Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST
	 * <br /><br />
	 * For example,
	 * <br />
	 * <b>Input:</b> root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
	 * <br />
	 * <b>Output:</b> 6
	 * <br />
	 *
	 * @static
	 * @function
	 * @see {@link https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/|Lowest Common Ancestor of a Binary Search Tree}
	 *
	 * @public
	 *
	 * @param {TreeNode} root root of binary search tree
	 * @param {TreeNode} p First tree node
	 * @param {TreeNode} q Second tree node
	 *
	 * @returns {number} Lowest common ancestor between two nodes
	 */

	static lowestCommonAncestor(
		root: TreeNode<number> | null,
		p: TreeNode<number>,
		q: TreeNode<number>
	): number | undefined {
		function _lowestCommonAncestor(
			root: TreeNode<number> | null,
			_p: TreeNode<number>,
			_q: TreeNode<number>
		): number | undefined {
			if (!root) return;
			if (p.value < root.value && q.value < root.value) {
				return _lowestCommonAncestor(root.left, _p, _q);
			} else if (p.value > root.value && q.value > root.value) {
				return _lowestCommonAncestor(root.right, _p, _q);
			} else {
				return root.value;
			}
		}
		return _lowestCommonAncestor(root, p, q);
	}
}
