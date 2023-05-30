class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1 , 1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one
        
        
#         dict_ = { 1:1 , 2:2 } 
        
#         if n <= 2:
#             return n
        
#         if n in dict_:
#             return dict_[n]
        
#         k = self.climbStairs(n-1) + self.climbStairs(n-2)
        
#         dict_[n] = k
        
#         return dict_[n]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         memo = defaultdict(int)
#         def fib(self,n):
            
#             result = 0
#             if n <= 2:
#                 return n
            
#             print(memo[n-1])
            
#             if memo[n-1]:
#                 result += memo[n-1]
                
#             else:
#                 del memo[n-1]
#                 result += fib(self,n-1)
                
#             if memo[n-2]:
#                 result += memo[n-2]
                
#             else:
#                 del memo[n-2]
#                 result += fib(self,n-2)
            
#             memo[n] = result
            
#             return result
            
#         return fib(self,n)
