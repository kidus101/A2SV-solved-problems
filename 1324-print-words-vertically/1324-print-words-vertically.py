class Solution:
    def printVertically(self, s: str) -> List[str]:
        
       
        string_list = list()
        string_list =s.split(" ")
        output_list = list()
        columns = 0
        rows = len(string_list)
        
        for new_string in string_list:
            columns = max(columns ,len(new_string))
       

        for column in range(columns):
            word = []
            for row in range(rows):
                if column < len(string_list[row]):
                    word.append(string_list[row][column]) 
                else:
                    word .append(" ")
            
            output_list.append("".join(word).rstrip())
        return (output_list)  
    
    # TC: O(N^2) & SC = O(N)
        
       