class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) <= 1:
            return 0

        staircost = [-1]*(len(cost)+2)

        cost = [0] + cost + [0]

        staircost[-1] = cost[-1]
        staircost[-2] = cost[-2]

        for i in range(len(cost)-3,-1,-1):
            staircost[i] = min(staircost[i+1],staircost[i+2]) + cost[i]

        return min(staircost[0],staircost[1])





        