/**
 * <b>1-D Dynamic Programing</b>
 * List of common 1-D dynamic programing.
 *
 * @example
 * import { climbStairs } from '../../1d-dp';
 *
 * console.log(climbStairs(2)); // 2
 * console.log(climbStairs(3)); // 3
 * console.log(climbStairs(6)); // 13
 *
 * @author Gaurav Soni
 *
 * @module 1d-dp
 *
 */

/**
 * You are climbing a staircase. It takes n steps to reach the top.
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 * <br>
 * For example,
 * <br />
 * <b>Input:</b> n = 5
 * <br />
 * <b>Output:</b> 8
 * <br />
 * <b>Time Complexity for constructor:</b> O(n) <br />
 * <b>Space Complexity for constructor:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/climbing-stairs/|Climbing Stairs}
 *
 * @public
 *
 * @param {number} n number of steps to reach the top
 * @returns {number} Number of ways one can climb the stairs
 */

export function climbStairs(n: number): number {
	const dp = new Array(n);
	function minSteps(num: number): number {
		if (num === 0) return 1;
		if (num === 1) return 1;
		if (dp[num]) {
			return dp[num];
		}
		dp[num] = minSteps(num - 1) + minSteps(num - 2);
		return dp[num];
	}
	return minSteps(n);
}

/**
 * You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 * Once you pay the cost, you can either climb one or two steps.
 *
 * You can either start from the step with index 0, or the step with index 1.
 * Return the minimum cost to reach the top of the floor.
 * <br>
 * For example,
 * <br />
 * <b>Input:</b> cost = [10,15,20]
 * <br />
 * <b>Output:</b> 15
 * <br />
 * <b>Time Complexity for constructor:</b> O(n) <br />
 * <b>Space Complexity for constructor:</b> O(n) <br />
 *
 * @see {@link https://leetcode.com/problems/min-cost-climbing-stairs/|Min Cost Climbing Stairs}
 *
 * @public
 *
 * @param {number[]} cost All cost to reach the top
 * @returns {number} Minimum cost required to reach the top
 */

export function minCostClimbingStairs(cost: number[]): number {
	const dp = new Array(cost.length);
	function findMinCost(n: number) {
		if (n === 0) return cost[0];
		if (n === 1) return cost[1];
		if (dp[n]) return dp[n];
		const minCost = Math.min(
			findMinCost(n - 1) + cost[n],
			findMinCost(n - 2) + cost[n]
		);
		dp[n] = minCost;
		return dp[n];
	}
	return Math.min(findMinCost(cost.length - 1), findMinCost(cost.length - 2));
}
