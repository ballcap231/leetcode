class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r_count = 1
        r_char = chars[0]
        
        for r in range(1,len(chars) + 1):
            if r < len(chars) and r_char == chars[r]:
                r_count += 1
            else:
                chars[l] = r_char
                #inserting ints
                str_count = str(r_count)
                if r_count > 1:
                    for str_int in str_count:
                        l += 1
                        chars[l] = str_int
                l += 1
                r_count = 1
                r_char = chars[r] if r < len(chars) else ''
                
        return l