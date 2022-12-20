from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Using ASCII VALUE
        tsum = 0
        for i in t:
            tsum += ord(i)
        for j in s:
            tsum -= ord(j)
        return chr(tsum)
        
        # TC: O(N) and SC:O(1)
        
        
        s += t
#         countedString = Counter(s)
        
#         for key,value in countedString.items():
#             mininum =min(countedString[key])
#             return key
            
#         # TC: O(N) and SC:O(N)
        
#         ptr1 = 0 
#         ptr2 = len(s) - 1
        
#         if s[ptr]
        
        