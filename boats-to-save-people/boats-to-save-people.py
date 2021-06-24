class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #O(NlogN) time and O(N) or O(1) space depending on if in-place sort allowed
        people.sort()
        l,r = 0, len(people) - 1
        count = 0
        while l < r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            count += 1
        if l == r:
            count += 1
        return count
        
        
        
        
        # # Brute force
        # #O(N^2) time and O(N) space
        # people.sort(reverse = True)
        # visited = set()
        # boats = 0
        # for first_pos in range(len(people)):
        #     if first_pos not in visited:
        #         max_combo = people[first_pos]
        #         max_combo_second_pos = -1
        #         for second_pos in range(first_pos + 1, len(people)):
        #             if second_pos not in visited:
        #                 curr_combo = max_combo + people[second_pos]
        #                 if curr_combo <= limit and curr_combo > max_combo:
        #                     max_combo = curr_combo
        #                     max_combo_second_pos = second_pos
        #         if max_combo_second_pos > -1:
        #             visited.add(max_combo_second_pos)
        #         visited.add(first_pos)
        #         boats += 1
        # return boats
                