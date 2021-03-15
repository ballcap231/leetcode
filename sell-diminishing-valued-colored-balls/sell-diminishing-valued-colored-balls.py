class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        arr=sorted(Counter(inv).items(), reverse=True)+[(0,0)]
        ans, ind, width=0,0,0
        
        while orders>0:
            width += arr[ind][1]
            sell=min(orders, width * (arr[ind][0] - arr[ind+1][0]))
            whole, remainder= divmod(sell, width)
            ans += width*(whole*(arr[ind][0]+arr[ind][0]-(whole-1)))//2 + remainder*(arr[ind][0]-whole)
            orders -= sell
            ind += 1
        return ans % 1_000_000_007  

        
        
        
        
        
        
        
        
        
        

        
        
#         hq = []
#         profit = 0
#         for ball in inventory:
#             heapq.heappush(hq, -ball)
        
#         while orders:
#             ball_val = -heapq.heappop(hq)
#             all_ball_val = orders
#             if hq:
#                 all_ball_val = (ball_val + hq[0] + 1) // 2 * (ball_val - hq[0])
            
#             next_profit = min(all_ball_val, orders)
#             profit += next_profit
#             new_ball_val = ball_val - next_profit
#             if new_ball_val > 0:
#                 heapq.heappush(hq, -new_ball_val)
#             orders -= next_profit
#         return profit % (10 ** 9 + 7)
            