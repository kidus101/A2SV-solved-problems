class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowset = set({})
        colset = set({})
        rowlen = len(matrix)
        collen = len(matrix[0])
        for row in range(0, rowlen):
            for col in range(0, collen):
                if matrix[row][col] == 0:
                    rowset.add(row)
                    colset.add(col)
        
        rowset = list(rowset)
        colset = list(colset)
        
        for row in rowset:
            matrix[row] = [0] * len(matrix[row])
        for coloumns in colset:
            col = coloumns
            for row in range(rowlen):
                matrix[row][col] = 0
        
        """
        Do not return anything, modify matrix in-place instead.
        """
#let's create a rowset and col list inorder to find the index of teh row and column where a zero is present

# Why a set ? there may be 2 zeros in a same row or column so to avoid that we use the set

# looping through the rows and when we reach the rows same as the row_list we will make them all zeros
#               the same happens to the columns
#         row_length =len(matrix)
#         col_length = len(matrix[0])
#         row_set = set()
#         col_set = set()
        
#         for row in range(row_length):
#             for col in range(col_length):
#                 if matrix[row][col] == 0:
#                     row_set.add(row)
#                     col_set.add(col)
        
#         row_list = list(row_set)
#         col_list = list(col_set)
        
#         for row in row_list:
#                 matrix[row] = [0]*row_length
#         for column in col_list:
#             col = column
#             for row in range(row_length):
                
                # matrix[row][col] = 0
        # for row in range(row_length):
        #     for col in range(col_length):
        #         if matrix[1][col] == 0:
        #             matrix[col] = [0]* col_length
                
                    
                    