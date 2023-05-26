class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        def fib(self,n):
            
            result = 0
            if n <= 2:
                return n
            
            print(memo[n-1])
            
            if memo[n-1]:
                result += memo[n-1]
                
            else:
                del memo[n-1]
                result += fib(self,n-1)
                
            if memo[n-2]:
                result += memo[n-2]
                
            else:
                del memo[n-2]
                result += fib(self,n-2)
            
            memo[n] = result
            
            return result
            
        return fib(self,n)
