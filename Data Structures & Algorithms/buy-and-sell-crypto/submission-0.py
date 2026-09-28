class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,left=0,[]

        for i in range(1,len(prices)):
            left.append(prices[i-1])
            if prices[i]-min(left)>profit:
                bp=min(left)
                profit=prices[i]-bp
                
            else:
                continue
        return profit