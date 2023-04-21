class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        graph = defaultdict(list)
# changed edges to adjacency list
        for node1 , node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
          
        # print(graph)
        
        visited = set()

        def dfs(node, visited, graph):
            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    result = dfs(neighbour, visited, graph)

                    if result:
                        print("#")
                        return True
                    
                    
        return dfs(source,visited,graph)
    