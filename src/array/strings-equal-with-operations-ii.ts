/**
 * <b>LeetCode -  Array Problems</b>
 *
 * @example
 * import { checkStrings } from '../../array';
 *
 * console.log(checkStrings('abcdba', 'cabdab'); // true
 *
 * @author Gaurav Soni
 *
 * @module array
 *
 */

/**
 * @public
 *
 * The algo is based on the counting char pattern. For more details, check notes.
 *
 * <b>Time Complexity:</b> O(n) <br />
 * <b>Space Complexity:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/|Check if Strings Can be Made Equal With Operations II}
 *
 * @param {string} s1 string.
 * @param {string} s2 string
 * @returns {boolean} true if s1 can be made equal to s2 after operations, otherwise false
 *
 */
export function checkStrings(s1: string, s2: string): boolean {
	const s1MapEven = new Array(26).fill(0);
	const s2MapEven = new Array(26).fill(0);
	const s1MapOdd = new Array(26).fill(0);
	const s2MapOdd = new Array(26).fill(0);
	for (let index = 0; index < s1.length; index++) {
		if (index % 2 == 0) {
			s1MapEven[s1.charCodeAt(index) - 'a'.charCodeAt(0)]++;
			s2MapEven[s2.charCodeAt(index) - 'a'.charCodeAt(0)]++;
		} else {
			s1MapOdd[s1.charCodeAt(index) - 'a'.charCodeAt(0)]++;
			s2MapOdd[s2.charCodeAt(index) - 'a'.charCodeAt(0)]++;
		}
	}
	for (let index = 0; index < s1MapEven.length; index++) {
		if (
			s1MapEven[index] !== s2MapEven[index] ||
			s1MapOdd[index] !== s2MapOdd[index]
		)
			return false;
	}
	return true;
}
