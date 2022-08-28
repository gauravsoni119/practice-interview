import { TreeNode, AVLTree } from '../../ds/avl-tree';
describe('Node', () => {
	it('should  create a Node', () => {
		const node = new TreeNode('some data', null, null, 0);
		expect(node.value).toEqual('some data');
	});
});

describe('AVLTree', () => {
	it('should insert items into AVLTree', () => {
		const tree = new AVLTree<number>();
		tree.insert(4);
		tree.insert(2);
		tree.insert(7);
		expect(tree.root?.value).toEqual(4);
		expect(tree.root?.left?.value).toEqual(2);
		expect(tree.root?.right?.value).toEqual(7);
	});

	it('should invert the AVLTree', () => {
		const tree = new AVLTree<number>();
		tree.insert(4);
		tree.insert(2);
		tree.insert(7);
		tree.invert();
		expect(tree.root?.value).toEqual(4);
		expect(tree.root?.left?.value).toEqual(7);
		expect(tree.root?.right?.value).toEqual(2);
	});

	it('should return height the AVLTree', () => {
		const tree = new AVLTree<number | null>();
		tree.insert(9);
		tree.insert(3);
		tree.insert(20);
		tree.insert(15);
		tree.insert(7);
		expect(tree.getHeight()).toEqual(3);
	});

	it('should return diameter of the AVLTree', () => {
		const tree = new AVLTree<number | null>();
		tree.insert(5);
		tree.insert(3);
		tree.insert(4);
		tree.insert(2);
		tree.insert(1);
		expect(tree.getDiameter()).toEqual(3);
	});

	describe('isBalanced', () => {
		it('should return true if AVLTree is balanced', () => {
			const tree = new AVLTree<number | null>();
			tree.insert(5);
			tree.insert(6);
			tree.insert(3);
			tree.insert(2);
			expect(tree.isBalanced()).toEqual(true);
		});

		it('should return false if AVLTree is not balanced(all nodes right)', () => {
			const tree = new AVLTree<number | null>();
			tree.insert(5);
			tree.insert(6);
			tree.insert(7);
			tree.insert(8);
			expect(tree.isBalanced()).toEqual(false);
		});

		it('should return false if AVLTree is not balanced(all nodes left)', () => {
			const tree = new AVLTree<number | null>();
			tree.insert(5);
			tree.insert(4);
			tree.insert(3);
			tree.insert(2);
			expect(tree.isBalanced()).toEqual(false);
		});
	});

	describe('isSameTree', () => {
		it('should return true if both trees are same', () => {
			const tree1 = new AVLTree<number>();
			const tree2 = new AVLTree<number>();
			tree1.insert(2);
			tree1.insert(1);
			tree1.insert(3);
			tree2.insert(2);
			tree2.insert(1);
			tree2.insert(3);
			expect(AVLTree.isSameTree(tree1, tree2)).toEqual(true);
		});

		it('should return false if both trees are not same', () => {
			const tree1 = new AVLTree<number>();
			const tree2 = new AVLTree<number>();
			tree1.insert(2);
			tree1.insert(1);
			tree1.insert(3);
			tree2.insert(5);
			tree2.insert(6);
			tree2.insert(7);
			expect(AVLTree.isSameTree(tree1, tree2)).toEqual(false);
		});
	});
});
