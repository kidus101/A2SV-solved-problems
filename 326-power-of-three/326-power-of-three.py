class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n ==1:
            return True
        elif n < 1:
            return False
        
        elif n % 3 !=0:
            return False
        
        return self.isPowerOfThree(n/3)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        f
        
#         while (n >= 3):
#             if (n%3 != 0):return False
#             n = n /3
#         return n == 1
                
#             # Time:O(log3)
#             # Space:O(1)
        
#        # mx = 3 ** 19
#         # return n > 0 and mx % n == 0
#         # #Time:O(1)
#         # #Space:O(1)  
        
        
        
       
        