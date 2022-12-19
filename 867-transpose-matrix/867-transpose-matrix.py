class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        #Zipping the corrosponding indexes of the sublists and returning the New list
        return zip(*matrix)
    
#     # TC:O() & SC:O()

        
        
        
        
        
        
        
        
#         #         Brute Force Solution

#         output = []
        
#         # matrix = [[1,2,3],[4,5,6],[7,8,9]]
        
#         for i in range(len(matrix[0])):
#             subList = []
           
#             for j in range(len(matrix)):
#                 subList.append(matrix[j][i])
#             output.append(subList)
            
#         return output
# TC :O(N) & SC:O(1)
        
        
        
#        Initial Thought Process 
        # output = []
        # sublist = []
        # k = 0
        # i = 0
        # lengthMatrix = len(matrix)

# # [[1,2,3],[4,5,6],[7,8,9]]

#         while i < lengthMatrix:
#             while k < lengthMatrix:
#                 sublist.append(matrix[k][i]) 
#                 k += 1
               
#             output.append(sublist) 
    
#             k+=1
#         return output