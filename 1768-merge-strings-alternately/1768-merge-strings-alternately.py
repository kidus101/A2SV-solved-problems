class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ''
        
        for i in range(min(len(word1),len(word2))):
            result += word1[i] + word2[i]
            
        return result + word1[i+1:] + word2[i+1:]
        
        
        
        
        
        
        
        # initial thought 
#         ptr1 = 0
#         ptr2 = len(word1)
#         string_list = list()
#         output = ""
        
#         newString = word1 + word2 # String contacenation
        
#         while ptr2 < len(newString) : 
#            if ptr1 < len(word1) and ptr2 < len(word2):
#                string_list.append(newString[ptr1])
#                string_list.append(newString[ptr2])
#                ptr1 += 1
#                ptr2 += 1

#         output = ''.join(string_list) 
#         return output
        
       
            
            

        
            
        
