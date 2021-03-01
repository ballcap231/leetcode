class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # map_website = defaultdict(list)
        # for t, u, w in sorted(zip(timestamp, username, website)):
        #     print(t,u,w)
        # return []
        
        map_website = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website), key = lambda x: (x[0],x[1])):
            map_website[u].append(w)
        counts = Counter()
        max_count = 0
        for user, websites in map_website.items():
            combos = itertools.combinations(websites, 3)
            for combo in set(combos):
                counts[combo] += 1
                max_count = max(max_count, counts[combo])
        
        candidates = []
        for combo, count in counts.items():
            if count == max_count:
                candidates.append(combo)
        
        return sorted(candidates)[0]
        
        