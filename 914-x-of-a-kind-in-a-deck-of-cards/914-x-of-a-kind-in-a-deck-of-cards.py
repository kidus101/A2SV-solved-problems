from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        counts = list(Counter(deck).values())
        
        
        gcd_cur = counts[0]
        
        for count in counts:
            gcd_cur = gcd(gcd_cur, count)
        
        if gcd_cur >= 2:
            return True
        else:
            return False
    
