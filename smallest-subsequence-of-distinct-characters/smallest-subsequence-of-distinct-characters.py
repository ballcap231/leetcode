class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Stack
        #O(N) time and O(1) space
        seen_chars = set()
        furthest_pos = {char:pos for pos, char in enumerate(s)}
        stack = []
        for pos in range(len(s)):
            if s[pos] not in seen_chars:
                while stack and stack[-1] > s[pos] and furthest_pos[stack[-1]] > pos:
                    seen_chars.discard(stack.pop())
                stack.append(s[pos])
                seen_chars.add(s[pos])
        return ''.join(stack)
        