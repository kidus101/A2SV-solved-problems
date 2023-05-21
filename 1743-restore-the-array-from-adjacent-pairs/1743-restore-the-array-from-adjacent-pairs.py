class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for u , v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque()
        for key in indegree:
            if indegree[key] == 1:
                queue.append(key)
                indegree[key] -= 1
                break    

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            
            for val in graph[node]:
                if indegree[val] == 2:
                    queue.append(val)
                    indegree[val] -= 2
        
        for key in indegree:
            if indegree[key] == 1:
                res.append(key)
                break

        return res