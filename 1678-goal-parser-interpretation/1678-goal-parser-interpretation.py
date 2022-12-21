class Solution:
    def interpret(self, command: str) -> str:
        string = ""
        charList = list()
        
        table ={
           "G" : "G",
            "()" :"o",
            "(al)" : "al"
        }
        
        for character in command:
            string += character
            if string in table:
                charList.append(table[string])
                string = ""
        return  "".join(charList)
    
    # TC: O(N) & SC:O(1)