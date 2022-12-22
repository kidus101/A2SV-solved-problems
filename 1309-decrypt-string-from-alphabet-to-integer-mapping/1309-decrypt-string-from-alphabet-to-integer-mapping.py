class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        string_list = list()
        
        d = { '1' : 'a', '2' : 'b', '3' : 'c', '4' : 'd', '5' : 'e', '6' : 'f', '7' : 'g','8' : 'h', '9' : 'i', '10#': 'j', '11#': 'k', '12#': 'l', '13#' : 'm', '14#': 'n', '15#': 'o','16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w','24#': 'x', '25#': 'y', '26#': 'z'}
        

        
        while i>= 0 :
            if s[i] == "#":
                string_list.append(d[s[i-2:i+1]])
                i -= 3
            else:
                string_list.append(d[s[i]])
                i-= 1
            
                
        return ''.join(string_list[::-1])
    
    # TC:O(N) & SC:O(1)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for i in range(::-1):
#             string += char 
            
#             if string in char_table:
#                 stringList.append(char_table[string])
#                 string = ""
                
#         return ''.join(string)
                