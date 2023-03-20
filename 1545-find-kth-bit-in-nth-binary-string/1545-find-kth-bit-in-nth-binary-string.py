class Solution:

    def findKth(self, n, k):
        
        if n == 1:
            return 0

        past_lenght = ((2 ** (n-1)) - 1)
        
        if k - (past_lenght) == 1:
            return 1

        if k <= (past_lenght):
            ans = self.findKth(n-1, k)
            
        else:
            ans = 1 - self.findKth(n-1, 2 * (past_lenght + 1) - k)

        return ans

    def findKthBit(self, n: int, k: int) -> str:
        return str(self.findKth(n,k))
            
         