class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minnum = 100
        maxReturn = 0
        for i in range(len(prices)):
            if prices[i] < minnum:
                minnum = prices[i]
                print("min:",minnum)
            elif prices[i] - minnum > maxReturn:
                maxReturn = prices[i] - minnum
                print("max:",maxReturn)
        return maxReturn