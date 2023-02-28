class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # O(logN) SC:O(N)
        
        if n == 1:
            return True
        
        elif n < 1:
            return False
        
        return self.isPowerOfFour(n/4)