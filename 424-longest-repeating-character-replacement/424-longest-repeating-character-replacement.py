class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
                    
        left = 0
        output = 0

        dic = defaultdict(int)

        for right in range(len(s)):

            curr = s[right]

            dic[curr] += 1
            
            while (right - left + 1) - max(dic.values()) > k:
                
                dic[s[left]] -= 1
                left += 1
            
            output = max(output, right - left + 1)
            
        return output
        