class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        paren = []
        ret = []
        to_keep = set()
        for pos, char in enumerate(s):
            if char == '(':
                paren.append((char, pos))
            elif char == ')':
                if paren and paren[-1][0] == '(':
                    prev_char, prev_pos = paren.pop()
                    to_keep.add(prev_pos)
                    to_keep.add(pos)
                else:
                    paren.append((char, pos))
        
                    
        for pos, char in enumerate(s):
            if char in "()":
                if pos in to_keep:
                    ret.append(char)
            else:
                ret.append(char)
        
        return ''.join(ret)