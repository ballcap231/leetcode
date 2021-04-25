class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {char: pos for pos, char in enumerate(order)}
        def is_sorted(left_word, right_word):
            for pos, char in enumerate(left_word):
                if pos >= len(right_word) or table[char] > table[right_word[pos]]:
                    return False
                elif table[char] < table[right_word[pos]]:
                    return True
            return True
            
        for word_pos in range(1, len(words)):
            if not is_sorted(words[word_pos - 1], words[word_pos]): return False
        return True
            