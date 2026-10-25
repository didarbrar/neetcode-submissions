class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=[0 for _ in range(len(prices))]
        mini=2**31
        for i in range(1,len(prices)):
            min_price[i]=min(mini,prices[i-1])
            mini=min(min_price[i],mini)
        max_profit=0
        for i in range(1,len(prices)):
            max_profit=max(max_profit,prices[i]-min_price[i])
        return (max_profit)
