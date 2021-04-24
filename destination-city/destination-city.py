class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outs = Counter()
        
        for from_, to_ in paths:
            outs[from_] += 1
            outs[to_] += 0
        
        for city,out_nodes in outs.items():
            if out_nodes == 0:
                return city