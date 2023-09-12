/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { threeSumClosest } from '../../array';
 *
 * console.log(threeSumClosest([-1,2,1,-4], 1); // 2
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the two pointer approach and is similar to 3sum. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n^2) <br />
 * <b>Space Complexity:</b> O(1) <br />
 *
 * @see {@link https://leetcode.com/problems/3sum-closest/description/|3Sum Closest}
 *
 * @param {number[]} nums array of numbers.
 * @param {number} target to which triplet should be closest.
 * @returns {number} array of triplet that results in closest to target
 */
export function threeSumClosest(nums: number[], target: number): number {
	let closest = nums[0] + nums[1] + nums[2];
	nums.sort((a, b) => a - b);
	for (let index = 0; index < nums.length; index++) {
		if (index > 0 && nums[index] == nums[index - 1]) continue;
		const num = nums[index];
		let left = index + 1;
		let right = nums.length - 1;
		while (left < right) {
			const sum = nums[left] + nums[right] + num;
			if (sum == target) {
				return sum;
			}
			if (Math.abs(sum - target) < Math.abs(target - closest)) {
				closest = sum;
			}
			if (sum > target) {
				right--;
			} else {
				left++;
			}
		}
	}
	return closest;
}
