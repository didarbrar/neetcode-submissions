class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ban=max(piles)
        left=1
        right=max_ban
        while left<=right:
            mid=(left+right)//2
            mid_value=0
            for ban in piles:
                if ban%(mid)==0:
                    mid_value+=ban//(mid)
                else:
                    mid_value+=(ban//(mid))+1
            if mid_value<=h:
                right=mid-1
            else:
                left=mid+1
        return left

        