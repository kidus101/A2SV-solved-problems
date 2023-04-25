class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if not edges:
            return []
        
        indegree = dict()
        
        for i in range(n):
            indegree[i] = 0
            
        for x , y in edges:
            indegree[y] += 1
            
        result =[]
        
        for key , value in indegree.items():
            if value == 0:
                result.append(key)
                
        return (result)
        
        
