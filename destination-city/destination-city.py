class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_set = set()
        to_set = set()
        for ls in paths:
            from_set.add(ls[0])
            to_set.add(ls[1])
        city = to_set.difference(from_set)
        return city.pop()