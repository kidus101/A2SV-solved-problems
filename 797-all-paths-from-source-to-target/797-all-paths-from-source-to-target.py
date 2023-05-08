class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        visited = set()

        def dfs(start, end, path):
            
            if start == end:
                val = path[:] + [start]
                ans.append(val)
                return
            
            visited.add(start)
            path.append(start)
            
            for node in graph[start]:   
                if node not in visited:
                    dfs(node, end, path)
            
            path.pop()
            visited.remove(start)

        dfs(0, len(graph)-1 ,[])
        return ans