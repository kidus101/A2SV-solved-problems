class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        x = str(x)
        ptr1 = 0
        ptr2 = len(str(x))-1
        
        
        # if len(str(x)) != len(str(y)):
        #     return False
        
        if len(x) == 1:
            return True
        while ptr1 < ptr2:
            if x[ptr1] == x[ptr2]:
                ptr1 += 1
                ptr2 -= 1
           
            else:
                return False
        return True
        
        # TC:O(N) & SC:O(1)
        
        
        
        
        
        
        
        
        
        
        #         y = x
        
#         x =121
#         y = -121
        
#         ptr1 = 0
#         ptr2 = len(str(y))-1
        
        # if len(str(x)) != len(str(y)):
        #     return False
        
#         while ptr1 < len(str(x)) and ptr2 > 0:
#             if x[ptr1] == y[ptr2]:
#                 ptr1 += 1
#                 ptr2 -= 1
#             else:return False
            
#         return True 
        