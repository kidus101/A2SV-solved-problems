class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Time:O(N) & Space:O(NlogN)
        
        piles.sort()
        i = len(piles)-2
        len_piles =len(piles)
        max_coins = 0
        
        while i > len_piles/3 - 1:
            max_coins += piles[i]
            i -= 2
        return max_coins