class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        output = []
        dict = {}
        
        for idx,char in enumerate(s):
            dict[char]=idx
            
        start = 0
        end = 0
        size = 0
        
        for idx,char in enumerate(s):
            size += 1
            end = max(end,dict[char])
            
            if(idx==end):
                output.append(size)
                size = 0
                
        return output