class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        outs = defaultdict(list)
        ins = defaultdict(list)
        for ticket in tickets:
            outs[ticket[0]].append(ticket[1])
            ins[ticket[1]].append(ticket[0])
        
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