class Solution:
    
 


    def findGCD(self,  nums: List[int]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        min_num = min(nums)  
        max_num = max(nums)
        
        return gcd(min_num , max_num)
    
        

   
        
        


