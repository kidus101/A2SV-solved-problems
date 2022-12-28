class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        return n if n%2 == 0 else n*2
        
        # TC:O(1) & SC:O(1)
        