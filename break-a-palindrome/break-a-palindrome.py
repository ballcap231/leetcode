class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ll = len(palindrome)
        if ll < 2:
            return ""
        for pos in range(ll // 2):
            if palindrome[pos] != 'a':
                return palindrome[:pos] + 'a' + palindrome[pos + 1:]
        return palindrome[:-1] + 'b'