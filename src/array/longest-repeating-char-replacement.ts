/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { characterReplacement } from '../../array';
 *
 * console.log(characterReplacement('ABAB', 2); // 4
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
 * @see {@link https://leetcode.com/problems/longest-repeating-character-replacement/|Longest Repeating Character Replacement}
 *
 * @param {string} s string.
 * @param {k} k number upto which max replacements are allowed
 * @returns {number} length of the longest substring
 *
 */
export function characterReplacement(s: string, k: number): number {
	let left = 0;
	let right = 0;
	let res = 0;
	const map = new Map();
	while (right < s.length) {
		if (!map.has(s[right])) {
			map.set(s[right], 1);
		} else {
			map.set(s[right], map.get(s[right]) + 1);
		}
		const count = Math.max(...map.values());
		while (right - left + 1 - count > k) {
			map.set(s[left], map.get(s[left]) - 1);
			left++;
		}
		res = Math.max(res, right - left + 1);
		right++;
	}
	return res;
}
