class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #O(N^2) time and O(N) space
        #Recursive DFS
        
        # seen = set()
        # def dfs(node):
        #     for count, val in enumerate(isConnected[node]):
        #         if val and count not in seen:
        #             seen.add(count)
        #             if count != node:
        #                 dfs(count)
        # ans = 0
        # for val in range(len(isConnected)):
        #     if val not in seen:
        #         dfs(val)
        #         ans += 1
        # return ans
    
        #Iterative BFS
        #O(N^2) time and O(N) space
        
        seen = set()
        self.qq = deque()
        def dfs(kk):
            self.qq.append(kk)
            while self.qq:
                popped = self.qq.popleft()
                for pos, is_one in enumerate(isConnected[popped]):
                    if is_one and pos not in seen:
                        seen.add(pos)
                        if pos != kk:
                            self.qq.append(pos)
        tot = 0
        for nn in range(len(isConnected)):
            if nn not in seen:
                dfs(nn)
                tot += 1
        return tot
        