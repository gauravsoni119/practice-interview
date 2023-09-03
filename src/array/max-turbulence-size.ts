/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { maxTurbulenceSize } from '../../array';
 *
 * console.log(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]); // 5
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the Kadane's algo and sliding window pattern. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/longest-turbulent-subarray/|Longest Turbulent Subarray}
 *
 * @param {number[]} arr array of numbers.
 * @returns {number} Length of subarray with maximum turbulence
 *
 */
export function maxTurbulenceSize(arr: number[]): number {
	let max = 1;
	let left = 0;
	let right = 1;
	let lastSign = '';
	while (right < arr.length) {
		if (arr[right - 1] < arr[right] && lastSign !== '<') {
			max = Math.max(max, right - left + 1);
			right++;
			lastSign = '<';
		} else if (arr[right - 1] > arr[right] && lastSign !== '>') {
			max = Math.max(max, right - left + 1);
			right++;
			lastSign = '>';
		} else {
			lastSign = '';
			if (arr[right] == arr[right - 1]) {
				right++;
			}
			left = right - 1;
		}
	}
	return max;
}
