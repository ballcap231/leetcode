class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x < 10:
            return True
        
        l,r = x, 0
        
        while l > r:
            l, rem = divmod(l, 10)
            r = r * 10 + rem

        return l == r or l == r//10
