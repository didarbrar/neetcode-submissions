class Solution:
    def trap(self, height: List[int]) -> int:
        amount=0
        n=len(height)
        prefix=[0 for _ in range(n)]
        suffix=[0 for _ in range(n)]
        for i in range(1,n):
            prefix[i]=max(prefix[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            suffix[i]=max(suffix[i+1],height[i+1])
        for i in range(n):
            if prefix[i]<=height[i]:
                amount+=0
            elif suffix[i]<=height[i]:
                amount+=0
            elif prefix[i]>=suffix[i]:
                amount+=min(prefix[i],suffix[i]-height[i])
            elif suffix[i]>prefix[i]:
                amount+=min(prefix[i]-height[i],suffix[i])
        return amount


        