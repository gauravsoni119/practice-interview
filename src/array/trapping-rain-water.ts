/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { trap } from '../../array';
 *
 * console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]); // 6
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the prefix sum approach. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 * <b>Space Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/trapping-rain-water/|Trapping Rain Water}
 *
 * @param {number[]} height to define height at each point.
 * @returns {number} Total trapped rain water
 */
export function trap(height: number[]): number {
	const maxPrefix = new Array(height.length);
	const maxSuffix = new Array(height.length);
	let res = 0;
	maxPrefix[0] = height[0];
	maxSuffix[height.length - 1] = height[height.length - 1];
	for (let index = 1; index < height.length; index++) {
		maxPrefix[index] = Math.max(height[index], maxPrefix[index - 1]);
	}
	for (let index = height.length - 2; index >= 0; index--) {
		maxSuffix[index] = Math.max(height[index], maxSuffix[index + 1]);
	}
	for (let index = 0; index < height.length; index++) {
		const trappedWater =
			Math.min(maxPrefix[index], maxSuffix[index]) - height[index];
		if (trappedWater >= 0) {
			res += trappedWater;
		}
	}
	return res;
}
