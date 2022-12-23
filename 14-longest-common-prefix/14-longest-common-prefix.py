class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix_set = set()
        common_prefix = ""
        _min = float("inf")
        
        for k in range(len(strs)):
            _min = min(_min,len(strs[k]))
        
        for i in range(_min):
            prefix_set = set()
            for j in range(len(strs)):
                prefix_set.add(strs[j][i])
            # print(prefix_set)
            if len(prefix_set) == 1 :
                common_prefix +=  "".join(prefix_set)
            else:
                return common_prefix
                
        return common_prefix
            
            