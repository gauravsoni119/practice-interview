/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { getAverages } from '../../array';
 *
 * console.log(getAverages([7,4,3,9,1,8,5,2,6], 3); // [-1,-1,-1,5,4,4,-1,-1,-1]
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the sliding window pattern. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/k-radius-subarray-averages/|K Radius Subarray Averages}
 *
 * @param {number[]} nums array of numbers.
 * @param {k} k radius around which average needs to be calculated.
 * @returns {number} List of average of k radius
 *
 */
export function getAverages(nums: number[], k: number): number[] {
	let left = 0;
	let right = 0;
	const res = new Array(nums.length).fill(-1);
	let sum = 0;
	while (right < nums.length) {
		sum += nums[right];
		if (right - left + 1 >= k * 2 + 1) {
			const avg = k * 2 + 1;
			res[left + k] = Math.floor(sum / avg);
			sum -= nums[left];
			left++;
		}
		right++;
	}
	return res;
}

export function getAveragesV1(nums: number[], k: number): number[] {
	if (k == 0) return nums;
	const prefixSum = new Array(nums.length + 1).fill(0);
	const res = new Array(nums.length).fill(-1);
	for (let index = 0; index < nums.length; index++) {
		prefixSum[index + 1] = prefixSum[index] + nums[index];
	}
	console.log(prefixSum);
	for (let index = k; index < nums.length - k; index++) {
		const sum = prefixSum[index + k + 1] - prefixSum[index - k];
		res[index] = Math.floor(sum / (k * 2 + 1));
	}
	return res;
}
