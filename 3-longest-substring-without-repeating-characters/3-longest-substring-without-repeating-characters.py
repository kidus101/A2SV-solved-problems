class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TC:O(N) SC:O(N)
        char_set = set()
        max_len = 0
        left = 0
        len_set = 0
        
        
        for char in s:

            while char in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(char)

            max_len = max(max_len,len(char_set))

        return max_len
        
#         for char in s:
#             if char not in char_set:
#                 char_set.add(char)
#             # len_set = len(set)
#             max_len = max(max_len,len(char_set))
            
#             while char in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#         return max_len
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         charSet = set()
#         left = 0
#         result = 0
        
#         for right in range(len(s)):
#             while s[right] in charSet:
#                 charSet.remove(s[left])
#                 left += 1
#             charSet.add(s[right])
#             result=max(result , right - left + 1)
            
#         return result
    
    # Time:O(N) Space:O(N)
        