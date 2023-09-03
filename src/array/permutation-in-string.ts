/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { checkInclusion } from '../../array';
 *
 * console.log(checkInclusion('ab', 'eidbaooo'); // true
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the fixed sliding window pattern. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/permutation-in-string/|Permutation in String}
 *
 * @param {string} s1 string.
 * @param {string} s2 string
 * @returns {boolean} true if s1 is permutation of s2, otherwise false
 *
 */
export function checkInclusion(s1: string, s2: string): boolean {
	const s1Map = new Array(26).fill(0);
	const s2Map = new Array(26).fill(0);
	let left = 0;
	let right = 0;
	for (let index = 0; index < s1.length; index++) {
		s1Map[s1.charCodeAt(index) - 'a'.charCodeAt(0)]++;
	}
	while (right < s2.length) {
		s2Map[s2.charCodeAt(right) - 'a'.charCodeAt(0)]++;
		const window = right - left + 1;
		if (window == s1.length && isSame(s1Map, s2Map)) return true;
		if (window >= s1.length) {
			s2Map[s2.charCodeAt(left) - 'a'.charCodeAt(0)]--;
			left++;
		}
		right++;
	}
	return false;
}

function isSame(s1Map: number[], s2Map: number[]): boolean {
	for (let index = 0; index < s1Map.length; index++) {
		if (s1Map[index] !== s2Map[index]) return false;
	}
	return true;
}
