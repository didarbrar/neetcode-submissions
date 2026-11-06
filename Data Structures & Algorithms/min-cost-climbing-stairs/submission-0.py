class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost)==1:
            return 0
        total=[0 for _ in range(len(cost)+1)]
        total[0]=0
        total[1]=0
        for i in range(2,len(cost)+1):
            total[i]=min(total[i-2]+cost[i-2],total[i-1]+cost[i-1])
        return total[len(cost)]
        