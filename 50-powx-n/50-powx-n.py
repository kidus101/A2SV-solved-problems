class Solution:
    def myPow(self, x: float, n: int) -> float:
        
            if n == 0:
                return 1
            
            if n < 0:
                n = abs(n)
                x = 1/x
                
            if n % 2 == 0:
                return self.myPow(x*x,n//2)
            
            if n % 2 != 0:
                return x * self.myPow(x*x,n//2)

       
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(x , n): 
#             if x == 0: return 0
#             if n == 0: return 1
            
#             result = helper(x , n//2)
#             result = result * result
#             return (x * result) if (n%2 != 0) else result
            
#         result = helper(x , abs(n))
        
#         return result if (n >= 0) else 1/result     
       
       
#         # Time:O()
#         # Space:O()
        