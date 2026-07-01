class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l=0
        r=1
        maxprofit=-100

        while (r<len(prices)):


            if prices[r]>=prices[l]:
                maxprofit = max(maxprofit, prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
        
        return max(0, maxprofit)




        