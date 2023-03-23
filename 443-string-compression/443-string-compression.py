class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
# 2 pointer one for the chars array and the other for the compressesd_arra
#  count compressed_array

        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(chars):
            count = 0
            letter = chars[ptr1]
            
            while ptr1 < len(chars) and chars[ptr1] == letter:
                count += 1
                ptr1 += 1
            
            chars[ptr2] = letter
            ptr2 += 1
            
            if count > 1 :
                for char in str(count):
                    chars[ptr2] = char
                    ptr2 += 1
            
        return ptr2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         i = 0
#         count = 1
        
#         for j in range(1 , len(chars)+1):
#             if j < len(chars) and chars[j] == chars[j - 1]:
#                 count += 1
#             else:
#                 chars[i] = chars[j -1]
#                 i += 1
                
#                 if count > 1:
#                     for k in str(count):
#                         chars[i] = k
#                         i += 1
#                     count = 1
#         return i
    
#     # TIme:O(n)
#     # Spcae:O(1)