class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])) :
                if target == matrix[row][col] :
                    return True
        return False
    
    # Time:O(m*n) and Space:O(1)