class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        
        
        if n == 0:
            return 0
        
        if n == 1 or n == 2:
            return 1
        
        return self.tribonacci(n-2) + self.tribonacci(n-1) + self.tribonacci(n-3)
        
        
#         if n <= 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 1
        
#         nums = [0 for i in range(n+1)]
#         nums[0] = 0
#         nums[1] = 1
#         nums[2] = 1
        
#         for i in range(3,n+1):
#             nums[i] = nums[i-1] + nums[i-2] + nums[i-3]
        
#         return nums[-1]
        
        
        