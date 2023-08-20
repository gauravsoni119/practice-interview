/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { countPairsOptimal } from '../../array';
 *
 * console.log(countPairsOptimal([-1,1,2,3,1]); // 2
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 * The algo is based on the two pointer approach. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/|Count Pairs Whose Sum is Less than Target}
 *
 * @public
 *
 * @param {number[]} nums array of numbers.
 * @returns {number} Number of pairs whose sum less than target
 */
export function countPairsOptimal(nums: number[], target: number): number {
	nums.sort((a, b) => a - b);
	let left = 0;
	let right = nums.length - 1;
	let res = 0;
	while (left < right) {
		if (nums[left] + nums[right] < target) {
			res += right - left;
			left++;
		} else {
			right--;
		}
	}
	return res;
}

export function countPairsBruteForce(nums: number[], target: number): number {
	let res = 0;
	for (let left = 0; left < nums.length; left++) {
		for (let right = left + 1; right < nums.length; right++) {
			const sum = nums[left] + nums[right];
			if (sum < target) {
				res++;
			}
		}
	}
	return res;
}
