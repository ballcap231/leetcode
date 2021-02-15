class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold, bought = 0, -prices[0]
        for day in range(1, len(prices)):
            sold = max(sold, bought + prices[day] - fee)
            bought = max(bought, sold - prices[day])
            
        return sold