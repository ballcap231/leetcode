class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        #O(NlogN + |inv|) time and O(N) space complexity where N is the # of unique numbers in inv 
        #|inv| represents the length of inv
        counts = sorted(Counter(inv).items(), reverse = True) + [(0,0)]
        ans,width, ind = 0,0,0
        while orders > 0:
            ball_val, ball_count = counts[ind][0], counts[ind][1]
            width += ball_count
            balls_to_add = min(orders, width * (ball_val - counts[ind + 1][0]))
            whole, remainder = divmod(balls_to_add, width)
            #Can't use int(my_number / 2) if numbers are too big. Longs would give inprecise values
            #since this uses floating-point arithmetic (i.e (IEEE-754 64-bit))
            #Must used floating-point division (i.e. my_number // 2)
            ball_vals_to_add = (width * (whole * (ball_val + ball_val - (whole - 1)))) // 2 + \
                                remainder * (ball_val - whole)
            ans += ball_vals_to_add
            orders -= balls_to_add
            ind += 1
        return ans % 1_000_000_007
            