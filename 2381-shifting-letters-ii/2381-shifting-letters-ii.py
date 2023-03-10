class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        list_ = [0]*(n + 1)
        res = ""
        
       
        for start, end, direction in shifts:
            
            if direction:
                list_[start] += 1
                list_[end + 1] -= 1
                
            else:
                list_[start] -= 1
                list_[end + 1] += 1
                    
       
        for idx in range(1, n):
            list_[idx] += list_[idx - 1]
        
        
        for idx in range(n):
            res += chr((ord(s[idx]) - ord('a') + list_[idx]) % 26 + ord('a'))
        
        return res