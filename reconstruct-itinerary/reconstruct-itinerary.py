class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Hierholzer's Algorithms
        outs = defaultdict(list)
        for ticket in tickets:
            outs[ticket[0]].append(ticket[1])
        
        for cities in outs:
            outs[cities].sort(reverse = True)
        
        self.ret = []
        def dfs(node):
            while outs[node]:
                out_node = outs[node].pop()
                dfs(out_node)
            self.ret.append(node)
            
        dfs("JFK")
        return self.ret[::-1]