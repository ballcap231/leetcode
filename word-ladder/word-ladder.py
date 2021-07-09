from string import ascii_lowercase
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words: return 0
        words.add(endWord)
        dq = deque([(beginWord, 1)])
        visited = set([beginWord])
        while dq:
            curr_node, depth = dq.popleft()
            for pos in range(len(curr_node)):
                for letter in ascii_lowercase:
                    new_word = curr_node[:pos] + letter + curr_node[pos + 1:]
                    if new_word not in visited:
                        if new_word == endWord:
                            return depth + 1
                        if new_word in words:
                            dq.append((new_word, depth + 1))
                            visited.add(new_word)
        
        return 0
                
        




# from itertools import combinations
# from collections import defaultdict, deque
# class Solution:
#     def hamming_distance(self, word_1, word_2):
#         dist = 0
#         pos = 0
#         while dist < 2 and pos < len(word_1):
#             if word_1[pos] != word_2[pos]:
#                 dist += 1
#             pos += 1
#         return dist
        
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         #O(M^2 * N) time, where M == |wordList| and N == |beginWord| - TLE
#         #O(M^2 * N) space
#         if endWord not in wordList: return 0
#         graph = wordList + [beginWord]
#         combos = combinations(graph, r = 2)
#         graph_dict = defaultdict(list)
#         for combo in combos:
#             if self.hamming_distance(combo[0], combo[1]) == 1:
#                 graph_dict[combo[0]].append(combo[1])
#                 graph_dict[combo[1]].append(combo[0])
        
#         dq = deque([(beginWord, 1)])
#         visited = set([beginWord])
        
#         while dq:
#             curr_word, depth = dq.popleft()
#             for child_node in graph_dict[curr_word]:
#                 if child_node == endWord:
#                     return depth + 1
#                 if child_node not in visited:
#                     visited.add(child_node)
#                     dq.append((child_node, depth + 1))
#         return 0