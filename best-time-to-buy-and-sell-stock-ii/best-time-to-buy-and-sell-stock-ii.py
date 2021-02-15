class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = 0
        # for pos in range(1, len(prices)):
        #     if prices[pos] > prices[pos - 1]:
        #         profits += prices[pos] - prices[pos - 1]
        # return profits
        
        
        
        
        if len(prices) < 2:
            return 0

        self.profits = 0

        def find_interval_for_one_trade(pos):
            #finds and returns the max profit for a given trade
            #starting from input pos
            #returns the next pos outside of this interval
            low, high = None, None
            while pos < len(prices) and (prices[pos] > high if high else True):
                price = prices[pos]
                if low is None or price <= low:
                    low = price
                elif high is None or price >= high:
                    high = price
                pos += 1
            if high and low is not None and high > low:
                self.profits += high - low
            return pos
        pos = 0
        while pos < len(prices):
            pos = find_interval_for_one_trade(pos)
        return self.profits
