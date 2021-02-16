class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        #Greedy soln?
        n = len(prices)
        if n < 2:
             return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans
    
    
#         #DP soln, O(N) time and O(1) space
#         sold, bought = 0, -prices[0]
#         for day in range(1, len(prices)):
#             sold = max(sold, bought + prices[day] - fee)
#             bought = max(bought, sold - prices[day])
            
#         return sold