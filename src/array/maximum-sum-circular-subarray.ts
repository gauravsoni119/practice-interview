/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { maxSubarraySumCircular } from '../../array';
 *
 * console.log(maxSubarraySumCircular([5,-3,5]); // 10
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the Kadane's algo. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/maximum-sum-circular-subarray/|Maximum Sum Circular Subarray}
 *
 * @param {number[]} nums array of numbers.
 * @returns {number} Max subarray sum in circular array
 */
export function maxSubarraySumCircular(nums: number[]): number {
	let total = 0;
	let globalMax = nums[0];
	let globalMin = nums[0];
	let currSum = 0;
	let currMin = 0;
	for (const num of nums) {
		total += num;
		currMin = Math.min(currMin, 0);
		currMin += num;
		globalMin = Math.min(currMin, globalMin);
		currSum = Math.max(currSum, 0);
		currSum += num;
		globalMax = Math.max(currSum, globalMax);
	}
	if (total == globalMin) return globalMax;
	return Math.max(globalMax, total - globalMin);
}
