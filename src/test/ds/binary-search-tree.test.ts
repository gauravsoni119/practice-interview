import { TreeNode, BinarySearchTree } from '../../ds/binary-search-tree';
describe('Node', () => {
	it('should  create a Node', () => {
		const node = new TreeNode('some data', null, null, 0);
		expect(node.value).toEqual('some data');
	});
});

describe('BinarySearchTree', () => {
	it('should insert items into BinarySearchTree', () => {
		const tree = new BinarySearchTree<number>();
		tree.insert(4);
		tree.insert(2);
		tree.insert(7);
		expect(tree.root?.value).toEqual(4);
		expect(tree.root?.left?.value).toEqual(2);
		expect(tree.root?.right?.value).toEqual(7);
	});

	it('should return lowest common ancestor between two nodes', () => {
		const tree = new BinarySearchTree<number>();
		const p = new TreeNode(2, null, null, 0);
		const q = new TreeNode(8, null, null, 0);
		const q1 = new TreeNode(4, null, null, 0);
		const p1 = new TreeNode(7, null, null, 0);
		const q2 = new TreeNode(9, null, null, 0);
		tree.insert(6);
		tree.insert(2);
		tree.insert(8);
		tree.insert(0);
		tree.insert(4);
		tree.insert(7);
		tree.insert(9);
		expect(BinarySearchTree.lowestCommonAncestor(tree.root, p, q)).toEqual(6);
		expect(BinarySearchTree.lowestCommonAncestor(tree.root, p, q1)).toEqual(2);
		expect(BinarySearchTree.lowestCommonAncestor(tree.root, p1, q2)).toEqual(8);
		expect(BinarySearchTree.lowestCommonAncestor(null, p1, q2)).toBeUndefined();
	});
});
