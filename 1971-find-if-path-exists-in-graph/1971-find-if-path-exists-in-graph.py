class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        default_dict = defaultdict(list)

        for node1 , node2 in edges:
            default_dict[node1].append(node2)
            default_dict[node2].append(node1)
            
        visited = set()

        def dfs(vertex, visited, default_dict):
            if vertex == destination:
                return True

            visited.add(vertex)

            for neighbour in default_dict[vertex]:
                if neighbour not in visited:
                    result = dfs(neighbour, visited, default_dict)
# What does checking result give us 
                    if result:
                        return True
                    
                    
        return dfs(source,visited,default_dict)
    