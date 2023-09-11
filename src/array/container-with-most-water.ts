/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { maxArea } from '../../array';
 *
 * console.log(maxArea([1,8,6,2,5,4,8,3,7]); // 49
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
 * <b>Time Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/container-with-most-water/|Container With Most Water}
 *
 * @param {number[]} height to define start and end of container.
 * @returns {number} Maximum container area
 */
export function maxArea(height: number[]): number {
	let max = 0;
	let left = 0;
	let right = height.length - 1;
	while (left < right) {
		const min = Math.min(height[left], height[right]);
		const area = (right - left) * min;
		max = Math.max(max, area);
		if (height[right] > height[left]) {
			left++;
		} else {
			right--;
		}
	}
	return max;
}
