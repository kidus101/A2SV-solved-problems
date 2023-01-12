class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        sub_list = list()
        
        for cols in range(len(strs[1])):
            string = ""
            
            for rows in range(len(strs)):
                string += strs[rows][cols]
                
            sub_list.append(string)
            
        count = 0   
        sorted_word = ""
        
        for word in sub_list:
            sorted_string = sorted(word)
            joined_string = "".join(sorted_string)
            
            if word != joined_string:
                count += 1
                
        return count
    
    # Time:O(N) and Space:O(1)