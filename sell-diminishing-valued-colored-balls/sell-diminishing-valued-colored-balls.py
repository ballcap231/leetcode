class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        counts = sorted(Counter(inv).items(), reverse = True) + [(0,0)]
        ans,width, ind = 0,0,0
        
        while orders > 0:
            ball_val, ball_count = counts[ind][0], counts[ind][1]
            width += ball_count
            balls_to_add = min(orders, width * (ball_val - counts[ind + 1][0]))
            whole, remainder = divmod(balls_to_add, width)
            ball_vals_to_add = width * (whole * (ball_val + ball_val - (whole - 1))) // 2 + \
                                remainder * (ball_val - whole)
            ans += ball_vals_to_add
            orders -= balls_to_add
            ind += 1
        return ans % 1_000_000_007
        
#         arr=sorted(Counter(inv).items(), reverse=True)+[(0,0)]
#         ans, ind, width=0,0,0
        
#         while orders>0:
#             ball_val,ball_count = arr[ind][0], arr[ind][1]
#             width += ball_count
#             sell=min(orders, width * (ball_val - arr[ind+1][0]))
#             whole, remainder= divmod(sell, width)
#             #arithmetic sum
#             ans += width*(whole*(ball_val + ball_val -(whole-1)))//2 + remainder*(ball_val-whole)
#             orders -= sell
#             ind += 1
#         return ans % 1_000_000_007
        
        
        
        

            