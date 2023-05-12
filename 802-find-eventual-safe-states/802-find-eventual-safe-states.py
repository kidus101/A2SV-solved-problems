class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        indegree=[0]*n
        adjacent=[[] for i in range(n)]
        
        for i in range(n): 
            
            indegree[i]=len(graph[i])
            for j in graph[i]:
                adjacent[j].append(i)
                
        queue = deque()
        result=[] * n
        
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                
        while queue:
            cur = queue.popleft()
            result.append(cur)
            
            for i in adjacent[cur]:
                if indegree[i]!=0:
                    indegree[i]-=1
                    
                if indegree[i]==0:
                    queue.append(i)
                    
        return sorted(result)