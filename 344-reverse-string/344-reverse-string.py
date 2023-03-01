class Solution:
    def reverseString(self, s: List[str]) -> None:
# TC:O(N) & SC:O(N)

#         Using Recurssion Method 2

        left = 0
        right = len(s) - 1
        
        def helper(left , right):
            
            if left >= right:
                return
        
            s[left] , s[right] = s[right] , s[left]

            return helper(left+1 , right-1)   
        
        helper(left,right)
        
        
        
#         Using Recurssion Method 1

#         left = 0
#         right = len(s) - 1
        
#         if left >= right:
#             return
        
#         s[left] , s[right] = s[right] , s[left]
#         left += 1
#         right -= 1
        
#         return self.reverseString(s[left:right+1])

        
#         left = 0
#         right = len(s)-1
#         # temp = int()
        
#         while left < right :
#             s[left] , s[right] = s[right] , s[left]
               
#             left += 1
#             right -= 1
            
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
       
            
            
            