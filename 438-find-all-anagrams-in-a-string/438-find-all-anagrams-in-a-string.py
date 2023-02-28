class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # TC:O(N) SC:O(N)
        
        p_dict = Counter(p)
        s_dict = defaultdict(int)
        output = []
        
        left = 0
        right = len(p)
        
        if len(p) > len(s):
            return output
        
        for i in range(len(p)):
            s_dict[s[i]] += 1
        
        while right < len(s):
            
            if s_dict == p_dict:
                output.append(left)
           
            s_dict[s[left]] -= 1
            
            if s_dict[s[left]] == 0:
                s_dict.pop(s[left])
                
            left += 1
           
            s_dict[s[right]] += 1
            right += 1 
            
        if s_dict == p_dict:
                output.append(left) 
        
        return output
        