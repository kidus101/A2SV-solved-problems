import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        array = []
        
        for i in range(n):
            for j in range(n):
                array.append(matrix[i][j])
        
        heapq.heapify(array)            
        
        for i in range(k - 1):      
            heapq.heappop(array)
            
        return heapq.heappop(array)