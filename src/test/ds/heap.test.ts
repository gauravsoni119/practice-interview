import { Heap } from '../../ds/heap';

describe('MinHeap', () => {
	it('should add items into MinHeap', () => {
		const minHeap = new Heap<number>((a, b) => b - a);
		minHeap.add(4);
		minHeap.add(2);
		minHeap.add(7);
		minHeap.add(9);
		minHeap.add(1);
		expect(minHeap.top).toEqual(1);
		minHeap.extract();
		minHeap.extract();
		expect(minHeap.top).toEqual(4);
	});
	it('should extract items from MinHeap', () => {
		const minHeap = new Heap<number>((a, b) => b - a);
		minHeap.add(4);
		minHeap.add(9);
		minHeap.add(1);
		minHeap.add(13);
		expect(minHeap.top).toEqual(1);
		minHeap.extract();
		expect(minHeap.top).toEqual(4);
		minHeap.extract();
		expect(minHeap.top).toEqual(9);
	});
	it('should throw error if MinHeap is empty and we try to extract', () => {
		const minHeap = new Heap<number>((a, b) => b - a);
		expect(() => minHeap.extract()).toThrow('The heap is already empty!');
	});
});

describe('MaxHeap', () => {
	it('should add items into MaxHeap', () => {
		const maxHeap = new Heap<number>();
		maxHeap.add(4);
		maxHeap.add(2);
		maxHeap.add(7);
		maxHeap.add(9);
		maxHeap.add(1);
		expect(maxHeap.top).toEqual(9);
		maxHeap.extract();
		maxHeap.extract();
		expect(maxHeap.top).toEqual(4);
	});
	it('should extract items from MaxHeap', () => {
		const maxHeap = new Heap<number>();
		maxHeap.add(4);
		maxHeap.add(9);
		maxHeap.add(1);
		maxHeap.add(13);
		expect(maxHeap.top).toEqual(13);
		maxHeap.extract();
		expect(maxHeap.top).toEqual(9);
		maxHeap.extract();
		expect(maxHeap.top).toEqual(4);
	});
	it('should throw error if MaxHeap is empty and we try to extract', () => {
		const maxHeap = new Heap<number>();
		expect(() => maxHeap.extract()).toThrow('The heap is already empty!');
	});
});

describe('Kth largest element', () => {
	it('should return kth largest element from heap', () => {
		const minHeap = Heap.kthLargestElement(3, [4, 5, 8, 2]);
		expect(minHeap.add(3)).toEqual(4);
		expect(minHeap.add(5)).toEqual(5);
		expect(minHeap.add(10)).toEqual(5);
		expect(minHeap.add(9)).toEqual(8);
		expect(minHeap.add(4)).toEqual(8);
	});
});

describe('Kth largest element', () => {
	it('should return weight of the last stone after smashing', () => {
		expect(Heap.lastStoneWeight([2, 7, 4, 1, 8, 1])).toEqual(1);
	});

	it('should return weight of the last stone after smashing', () => {
		expect(Heap.lastStoneWeight([2, 2])).toEqual(0);
	});
});
