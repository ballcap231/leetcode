class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'),float('-inf'),0
        
        for price in prices:
            prev_sold = sold
            sold = held + price
            held,reset = max(held, reset - price), max(reset, prev_sold)
            
        return max(reset,sold)
            
        