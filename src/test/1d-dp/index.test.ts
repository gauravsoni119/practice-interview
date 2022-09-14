import { climbStairs, minCostClimbingStairs } from '../../1d-dp';

describe('Climbing Stairs', () => {
	it('should return minimum number of steps required to climb stairs', () => {
		expect(climbStairs(2)).toEqual(2);
	});
	it('should return minimum number of steps required to climb stairs', () => {
		expect(climbStairs(3)).toEqual(3);
	});
	it('should return minimum number of steps required to climb stairs', () => {
		expect(climbStairs(6)).toEqual(13);
	});
});

describe('Min Cost Climbing Stairs', () => {
	it('should return minimum cost required to climb stairs', () => {
		expect(minCostClimbingStairs([10, 15, 20])).toEqual(15);
	});
	it('should return minimum number of steps required to climb stairs', () => {
		expect(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])).toEqual(
			6
		);
	});
});
