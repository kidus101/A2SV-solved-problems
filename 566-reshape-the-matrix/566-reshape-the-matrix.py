class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # TC: O(N*M) SC:(N)
       
        extended_list = list()
        
        # Changing the given matrix to a one long list 
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                extended_list.append(mat[row][col])
        
        reshaped_matrix = list()
        
        if len(extended_list) != r*c :
            return mat
#         For r rows we will calculate the column length's range and append to the new matrix
        else:
            for row_index in range(r):
                reshaped_matrix.append(extended_list[row_index*c: row_index*c+c])
            return reshaped_matrix

        
        
        
        
        
        
        
        
        
       
        