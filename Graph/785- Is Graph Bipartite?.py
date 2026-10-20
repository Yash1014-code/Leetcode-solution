class Solution:
    def dfs(self,curr_node,visited,graph,color):
        visited[curr_node]=color
        for adjnode in graph[curr_node]:
            if visited[adjnode]!=-1:
                if visited[adjnode]==color:
                    return False
            else:
                ans=self.dfs(adjnode,visited,graph,1-color)
                if ans==False:
                    return False
        return True                   
    def isBipartite(self, graph: List[List[int]]) -> bool:
        total_node=len(graph)
        visited=[-1]*total_node
        for i in range(0,total_node):
            if visited[i]==-1:
                ans=self.dfs(i,visited,graph,0)
                if ans==False:
                    return False
        return True            
        
