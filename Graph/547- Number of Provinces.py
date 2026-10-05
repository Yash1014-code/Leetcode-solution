class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list=[[] for i  in range(n)]
        for i  in range(0,n):
            for j in range(0,n):
                if i!=j and isConnected[i][j]==1:
                   adj_list[i].append(j)
        visited = set() 
        count = 0          
        def dfs(root):
            for node in adj_list[root]:
                if node not in visited:
                    visited.add(node)
                    dfs(node)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count+=1
        return count        
