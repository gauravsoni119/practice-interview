/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { threeSum } from '../../array';
 *
 * console.log(threeSum([-1,0,1,2,-1,-4]); // [[-1,-1,2],[-1,0,1]]
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the two pointer approach. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n^2) <br />
 * <b>Space Complexity:</b> O(1) <br />
 *
 * @see {@link https://leetcode.com/problems/3sum/description/|3Sum}
 *
 * @param {number[]} nums array of numbers.
 * @returns {number} array of triplet that results in 0
 */
export function threeSum(nums: number[]): number[][] {
	const res = [];
	nums.sort((a, b) => a - b);
	for (let index = 0; index < nums.length; index++) {
		if (index > 0 && nums[index - 1] == nums[index]) continue;
		const num = nums[index];
		let left = index + 1;
		let right = nums.length - 1;
		while (left < right) {
			const twoSum = nums[left] + nums[right];
			const threeSum = [num, nums[left], nums[right]];
			if (num + twoSum == 0) {
				res.push(threeSum);
				while (left < right && nums[left] == nums[left + 1]) left++;
				while (left < right && nums[right] == nums[right - 1]) right--;
				left++;
				right--;
			} else if (num + twoSum > 0) {
				right--;
			} else left++;
		}
	}
	return res;
}
