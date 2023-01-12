class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        # temp = int()
        
        while left < right :
            s[left] , s[right] = s[right] , s[left]
               
            left += 1
            right -= 1
            
            # temp = s[left]
            # s[left]=s[right] 
            # print(s[left])
            # s[right]  = temp
            
    # Time:O(N) Space:O(1)     
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s = ["h","e","l","l","o"]
        # s = [,"e","l","l","o"]----- 
        # temp="h"
        #      left             right
        #     temp = s[left] 
        #     s[left]=s[right] 
        #     s[left] = temp
            
#         left = 0
#         right = len(s)-1
        
#         while left < right :
#             #we need to swap s[left] and s[right]
#             # How? 
            
#             temp = s[left]
#             s[left]=s[right] 
#             s[right]  = temp
            
#             # Time:O(N) && Space:O(1)
            
#             # s[left] , s[right] = s[right] ,s[left]
            
#             left +=1
#             right -=1
       
            
            
            