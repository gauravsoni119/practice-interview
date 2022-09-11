/**
 * <b>Binary Heap</b>
 * A binary heap is the complete binary tree which satisfies the heap properties.
 *
 * @example
 * import { Heap } from '../../ds/heap';
 * const minHeap = new Heap<number>((a, b) => b - a);
 * minHeap.add(5);
 * minHeap.add(2);
 * minHeap.add(3);
 * minHeap.add(7);
 *
 * console.log(minHeap.top); // 2
 * console.log(minHeap.extract()); // 3
 * console.log(minHeap.extract()); // 5
 *
 * @author Gaurav Soni
 *
 * @module ds/heap
 *
 */

/**
 * Heap
 *
 *
 * @public
 * @constructor
 */
export class Heap<T> {
	public heap: T[] = [];
	private cmp: (a: number, b: number) => number = (a, b) => a - b;
	constructor(cmp?: (a: number, b: number) => number) {
		this.cmp = cmp ? cmp : this.cmp;
	}

	/**
	 * Add the value into the heap. <br /><br />
	 * <b>Time Complexity:</b> O(logN).
	 *
	 * @public
	 * @method
	 * @param {T} value value that needs to be inserted
	 * @returns void
	 */
	add(value: T): void {
		this.heap.push(value);
		this.changeKey(this.heap.length - 1, value);
	}

	/**
	 * Remove the top most item from the heap. <br /><br />
	 * <b>Time Complexity:</b> O(logN).
	 *
	 * @public
	 * @method
	 * @returns {value} The top most item from the heap
	 */
	extract(): T {
		if (!this.heap.length) {
			throw 'The heap is already empty!';
		}
		const removedItem = this.heap.shift() as T;
		this.heapify(0);
		return removedItem;
	}

	/**
	 * Getter to get the top most item in the heap
	 */
	get top(): T {
		return this.heap[0];
	}

	/**
	 * Getter to get the size of the heap
	 */
	get size(): number {
		return this.heap.length;
	}

	/**
	 * Change the value of the key. It will update the value according to the heap type(min/max). <br /><br />
	 * <b>Time Complexity:</b> O(logN).
	 *
	 * @public
	 * @method
	 * @returns {value} The top most item from the heap
	 *
	 */
	changeKey(index: number, value: T): void {
		this.heap[index] = value;
		let parent = this.getParentIndex(index);
		while (
			parent >= 0 &&
			this.cmp(this.heap[index] as number, this.heap[parent] as number) > 0
		) {
			this.swap(parent, index);
			index = parent;
			parent = this.getParentIndex(index);
		}
	}

	private heapify(index: number) {
		let extra = index;
		while (index < this.heap.length - 1) {
			const left = this.getLeftIndex(index);
			const right = this.getRightIndex(index);
			if (
				left < this.heap.length &&
				this.cmp(this.heap[left] as number, this.heap[index] as number) > 0
			) {
				extra = left;
			}
			if (
				right < this.heap.length &&
				this.cmp(this.heap[right] as number, this.heap[index] as number) > 0 &&
				this.cmp(this.heap[right] as number, this.heap[left] as number) > 0
			) {
				extra = right;
			}
			if (extra !== index) {
				this.swap(index, extra);
				index = extra;
			} else {
				return;
			}
		}
	}

	private getParentIndex(index: number): number {
		return Math.floor((index - 1) / 2);
	}

	private getLeftIndex(index: number): number {
		return Math.floor(index * 2 + 1);
	}

	private getRightIndex(index: number): number {
		return Math.floor(index * 2 + 2);
	}

	private swap(a: number, b: number): void {
		[this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
	}

	/**
	 * Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
	 * <br />Implement KthLargest class:<br />
	 * KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
	 * int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
	 * For example,
	 * <br />
	 * <b>Input:</b> ["KthLargest", "add", "add", "add", "add", "add"]
	 * [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
	 * <br />
	 * <b>Output:</b> [null, 4, 5, 5, 8, 8]
	 * <br />
	 * <b>Time Complexity for constructor:</b> O(n*log(k)) <br />
	 * T<b>ime Complexity for add function:</b> O(n*log(k))
	 *
	 * @method
	 * @see {@link https://leetcode.com/problems/kth-largest-element-in-a-stream/|Kth Largest Element in a Stream}
	 *
	 * @public
	 *
	 * @param {number} k kth position of the element that needs to be returned
	 * @param {number[]} nums Stream of numbers
	 * @returns {Object} Object containing add method which will maintain the heap of 'k' size.
	 */

	static kthLargestElement(
		k: number,
		nums: number[]
	): { add: (num: number) => number } {
		const minHeap = new Heap<number>((a, b) => b - a);
		for (const num of nums) {
			minHeap.add(num);
			if (minHeap.size > k) {
				minHeap.extract();
			}
		}
		return {
			add: (num) => {
				minHeap.add(num);
				if (minHeap.size > k) {
					minHeap.extract();
				}
				return minHeap.top;
			}
		};
	}

	/**
	 * You are given an array of integers stones where stones[i] is the weight of the ith stone.
	 * <br />Implement KthLargest class:<br />
	 * We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
	 * Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is: <br />
	 *  If x == y, both stones are destroyed, and <br />
	 *  If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
	 * At the end of the game, there is at most one stone left.
	 * Return the weight of the last remaining stone. If there are no stones left, return 0.
	 * For example,
	 * <br />
	 * <b>Input:</b> stones = [2,7,4,1,8,1]
	 * <br />
	 * <b>Output:</b> 1
	 * <br />
	 *
	 * <b>Time Complexity:</b> O(n*log(n)) <br />
	 *
	 * @method
	 * @see {@link https://leetcode.com/problems/last-stone-weight/|Last Stone Weight}
	 *
	 * @public
	 *
	 * @param {number[]} stones Stones where stones[i] is the weight of the ith stone.
	 * @returns {number} Weight of the last remaining stone.
	 */

	static lastStoneWeight(stones: number[]): number {
		const maxHeap = new Heap<number>();
		for (const stone of stones) {
			maxHeap.add(stone);
		}
		while (maxHeap.size > 1) {
			const x = maxHeap.extract();
			const y = maxHeap.extract();
			const diff = x - y;
			if (diff > 0) {
				maxHeap.add(diff);
			}
		}
		return maxHeap.size > 0 ? maxHeap.top : 0;
	}
}
