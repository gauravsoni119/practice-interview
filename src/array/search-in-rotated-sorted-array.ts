/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { searchInRotatedArray } from '../../array';
 *
 * console.log(searchInRotatedArray([4,5,6,7,0,1,2], 0)); // 4
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * <b>Time Complexity:</b> O(log(n)) <br />
 *
 * @see {@link https://leetcode.com/problems/search-in-rotated-sorted-array/|Search in rotated array}
 *
 * @public
 *
 * @param {number[]} nums array of numbers.
 * @param {number} target element to be searched.
 * @returns {number} Index of element otherwise -1
 */
export function searchInRotatedArray(nums: number[], target: number): number {
	let left = 0;
	let right = nums.length - 1;
	const n = nums.length;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (nums[mid] > nums[n - 1]) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	const index = binarySearch(0, left - 1);
	return index !== -1 ? index : binarySearch(left, n - 1);

	function binarySearch(left: number, right: number) {
		while (left <= right) {
			const mid = Math.floor((left + right) / 2);
			if (target == nums[mid]) return mid;
			if (target < nums[mid]) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		return -1;
	}
}

export function searchWithPivotAndShift(
	nums: number[],
	target: number
): number {
	let left = 0;
	let right = nums.length - 1;
	const n = nums.length;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (nums[mid] > nums[n - 1]) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}
	return binarySearch(left);

	function binarySearch(pivot: number) {
		const n = nums.length;
		let left = 0;
		let right = n - 1;
		while (left <= right) {
			const mid = Math.floor((left + right) / 2);
			if (target == nums[(pivot + mid) % n]) return (pivot + mid) % n;
			if (target < nums[(pivot + mid) % n]) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		return -1;
	}
}

export function searchWithOneBinarySearch(
	nums: number[],
	target: number
): number {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target == nums[mid]) return mid;
		if (nums[left] <= nums[mid]) {
			if (target < nums[left] || target > nums[mid]) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		} else {
			if (target > nums[right] || target < nums[mid]) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
	}
	return -1;
}
