/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { canMakeSubsequence } from '../../array';
 *
 * console.log(canMakeSubsequence('abc', 'ad'); // true
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
 * @see {@link https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/|Make String a Subsequence Using Cyclic Increments}
 *
 * @public
 *
 * @param {string} str1 main string.
 * @param {string} str2 substring
 * @returns {boolean} true if subsequence can be make out of str1, otherwise false
 */
export function canMakeSubsequence(str1: string, str2: string): boolean {
	let mainIndex = 0;
	let subSeqIndex = 0;
	while (mainIndex < str1.length && subSeqIndex < str2.length) {
		const strChar = str1.charCodeAt(mainIndex);
		const subStrChar = str2.charCodeAt(subSeqIndex);
		if (
			strChar == subStrChar ||
			strChar + 1 == subStrChar ||
			(str1[mainIndex] == 'z' && str2[subSeqIndex] == 'a')
		) {
			mainIndex++;
			subSeqIndex++;
		} else {
			mainIndex++;
		}
	}
	return subSeqIndex == str2.length;
}
