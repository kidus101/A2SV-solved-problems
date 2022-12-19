class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -= 1
        return True

# TC:O(N) && O(1)
        
         # Changing upper case to lowercase
        #using a white space delimiter to attach all strings together
# Using a while loop with start < end pointers inorder to check if every charachter is the same or not
# If it's an empty string theb it's a palindrom

# how can we remove All Non alpha-Numerical strings
       
#         newString = s.lower()
# #          Code for removing all non alphanumericals
        
#         start = 0
#         end = len(s) -1
        
#         if s == "":
#             return True
        
#         while start < end:
#             if s[start] == s[end]:
#                 start += 1
#                 end -= 1
            
#             else:
#                 return True
                
#         return True 
            
            
       
  
            
            
            