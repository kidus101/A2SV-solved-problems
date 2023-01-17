

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # TC :O(n*m) SC:(1)
        
        result = list()   
        top , bottom = 0 , len(matrix)
        left , right = 0 , len(matrix[0]) 
        
        # Base Condition
        while left < right and top < bottom   :
            
# Appending the first row and incrementing the top when finished    
            
            
            for col in range(left ,right):
                result.append(matrix[top][col])
            top += 1
            
# Appending the last column
            for row in range(top , bottom):
                result.append(matrix[row][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for col in range(right -1 , left-1 , -1):
                result.append(matrix[bottom - 1][col])
            bottom -= 1
            
            for row in range(bottom -1 , top -1, -1):
                result.append(matrix[row][left ])
            left += 1
            
            
        return result
            
            
                