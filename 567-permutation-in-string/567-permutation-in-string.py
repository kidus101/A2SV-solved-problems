class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# TC:O(N) & SC:O(N) 
        s1_dict = Counter(s1)
        s2_dict = defaultdict(int)
        output = []
        
        left = 0
        right = len(s1)
        
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            s2_dict[s2[i]] += 1
        
        while right < len(s2):
            
            if s1_dict == s2_dict:
                return True
            
            s2_dict[s2[left]] -= 1
            
            if s2_dict[s2[left]] == 0:
                s2_dict.pop(s2[left])
            
            left += 1
            
            s2_dict[s2[right]] += 1
            right += 1
        
        if s1_dict == s2_dict:
            return True
            
        return False
            