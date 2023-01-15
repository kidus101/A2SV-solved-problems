class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
 # Create an Algo that check the diagonals 
#         Use the abouve function for every row and col starting from 1 to end of col

        row_length= len(matrix) 
        col_length = len(matrix[0])
    
        def same_diagonal(row , col):
            number = matrix[row][col]
            
            while row < row_length and col < col_length:
                if matrix[row][col] != number:
                    return False
                
                row += 1
                col += 1
            return True
            
        
        for col in range(col_length):
            if not same_diagonal(0 , col):
                return False
            
        for row in range(1,row_length):
            if not same_diagonal(row , 0):
                return False
            
        return True
           
                    
        
        